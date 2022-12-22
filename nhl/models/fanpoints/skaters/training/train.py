import pandas as pd
import numpy as np
import data, data_prep, training

goalie_list = ['savePct']
skater_list = ['goals', 'shots', 'timeOnIce', 'ppTimeOnIce', 'fanPoints', 'points']
team_list = ['goalsAgainst', 'shotsAgainstPerGame']

df = data.main()
df = data_prep.main(df, goalie_list=goalie_list, skater_list=skater_list, team_list=team_list, per_sixty_list=None)

print(df.columns)

cat_var = input("Categorical Variables: ")

edf = training.ohe(df, cat_vars=cat_var)

print(edf.columns)

features = input("Feature List: ")
target = input("Target Variable: ")

training.trainer(df=edf, features=features, target=target, learning_rate=0.1, n_estimators=1500, max_depth=5, scale=True,save_model=False)


