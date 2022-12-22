import pandas as pd
import numpy as np
import data, data_prep, data_train

goalie_list = ['savePct']
skater_list = ['goals', 'shots', 'timeOnIce', 'ppTimeOnIce', 'fanPoints', 'points']
team_list = ['goalsAgainst', 'shotsAgainstPerGame']

df = data.main()
df = data_prep.main(df, goalie_list=goalie_list, skater_list=skater_list, team_list=team_list, per_sixty_list=None)

print(df.columns)

cat_var = ['homeRoad', 'positionCode', 'shootsCatches']
edf = data_train.ohe(df, cat_vars=cat_var)

print(edf.columns)

features = ['OpHomeDummy', 'OpRoadDummy', 'savePctLastGame', 'savePctMa3', 'savePctMa7','savePctMa16', 'goalsLastGame','goalsMa3', 'goalsMa7', 'goalsMa16', 'shotsLastGame', 'shotsMa3', 'shotsMa7', 'shotsMa16', 'timeOnIceLastGame', 'timeOnIceMa3', 'timeOnIceMa7', 'timeOnIceMa16', 'ppTimeOnIceLastGame','ppTimeOnIceMa3', 'ppTimeOnIceMa7','ppTimeOnIceMa16', 'fanPointsLastGame','fanPointsMa3', 'fanPointsMa7','fanPointsMa16', 'pointsLastGame','pointsMa3', 'pointsMa7','pointsMa16','goalsAgainstLastGame','goalsAgainstMa3','goalsAgainstMa7', 'goalsAgainstMa16', 'shotsAgainstPerGameLastGame','shotsAgainstPerGameMa3', 'shotsAgainstPerGameMa7','shotsAgainstPerGameMa16', '0', '1', '2', '3', '4', '5', '6', '7']
target = input("Target Variable: ")

data_train.trainer(df=edf, features=features, target=target, learning_rate=0.1, n_estimators=1500, max_depth=5, scale=True,save_model=True)


