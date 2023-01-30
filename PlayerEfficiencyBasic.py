import pandas as pd
import seaborn as sns
import numpy as np

from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import teams
from nba_api.stats.static import players
from nba_api.stats.endpoints import leaguedashteamshotlocations
from nba_api.stats.endpoints import shotchartdetail
teams = teams.get_teams()

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib.font_manager as fm
from matplotlib.patches import Circle, Rectangle, Arc, ConnectionPatch


#Pull player data
ja_id = next((x for x in players.get_players() if x.get("full_name") == "Ja Morant"), None).get("id")

gamelog_ja = pd.concat(playergamelog.PlayerGameLog(player_id=ja_id, season=SeasonAll.all).get_data_frames())
gamelog_ja["GAME_DATE"] = pd.to_datetime(gamelog_ja["GAME_DATE"], format="%b %d, %Y")
gamelog_ja = gamelog_ja.query("GAME_DATE.dt.year in [2021, 2023]")

#Create Dataframe
df = pd.DataFrame(data=gamelog_ja)
df[['WL','FGA','FG_PCT']]

#set coloring
colors = {'L':'lightcoral', 'W':'darkcyan'}
df.columns

#2d Scatterplot 
plt.scatter(df['FT_PCT'],df['PTS'],c=df['WL'].map(colors),s = [2*2*n for n in range(len(df['PTS']))])
plt.xlabel("FT_PCT")
plt.ylabel("FG_PCT")
plt.title("Ja FT% v FG%")
plt.legend(["Loss", "W"], loc ="lower right")
plt.show()

#3d scatterplotsetup
#select x/y/z data
z = df['FG_PCT']
x = df['PTS']
y = df['FT_PCT']
 
# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
# Creating plot
ax.scatter3D(x, y, z, color = df['WL'].map(colors),s = [2*2*n for n in range(len(df['PTS']))])
plt.title("Morant")
plt.xlabel("PTS")
plt.ylabel("FT_PCT")
plt.ylim(0.2,1.0)
ax.set_zlabel('FG_PCT')
# show plot
plt.show()
