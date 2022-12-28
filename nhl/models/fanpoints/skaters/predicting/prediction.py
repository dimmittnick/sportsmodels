import pandas as pd
import numpy as np
from datetime import *
import today_data
import sys
sys.path.append('../training')
import data, data_prep, data_train
from sklearn.preprocessing import RobustScaler
import joblib

## script that generates daily predictions
## run this in terminal and it will generate the predictions onto the desktop

daily_url = "https://www.rotowire.com/hockey/nhl-lineups.php"

nhl_teams = 'ANA ANH ARI BOS BUF CAR CGY CHI CLS CBJ COL DAL DET EDM FLA LA LAK MIN MON MTL NJ NSH NYI NYR OTT PHI PIT SEA SJ SJS STL TB TBL TOR VAN VGK WAS WPG'.split()

team_map = {'ANH':'ANA', 
            'ARI':'ARI', 
            'BOS':'BOS', 
            'BUF': 'BUF', 
            'CAR':'CAR', 
            'CGY':'CGY', 
            'CHI':'CHI', 
            'CLS': 'CBJ', 
            'COL':'COL', 
            'DAL':'DAL', 
            'DET':'DET', 
            'EDM':'EDM', 
            'FLA':'FLA', 
            'LA':'LAK', 
            'MIN':'MIN', 
            'MON': 'MTL', 
            'NJ':'NJD', 
            'NSH':'NSH', 
            'NYI':'NYI', 
            'NYR': 'NYR', 
            'OTT':'OTT', 
            'PHI':'PHI', 
            'PIT':'PIT', 
            'SEA':'SEA', 
            'SJ': 'SJS', 
            'STL': 'STL', 
            'TB':'TBL', 
            'TOR':'TOR', 
            'VAN':'VAN', 
            'VGK':'VGK', 
            'WAS':'WSH', 
            'WPG':'WPG'}

road_team_xpath = '/html/body/div[1]/div/main/div[3]//div//div//div//div//a[1]//div//text()'
home_team_xpath = '/html/body/div[1]/div/main/div[3]//div//div//div//div//a[2]//div//text()'

road_goalie_xpath = '/html/body/div[1]/div/main/div[3]//div//div//div//ul[1]//li[1]//div[1]/a[1]/text()'
home_goalie_xpath = '/html/body/div[1]/div/main/div[3]//div//div//div//ul[2]//li[1]//div[1]/a[1]/text()'

today = datetime.today().strftime("%Y-%m-%d")

goalie_list = ['savePct']
skater_list = ['goals', 'shots', 'timeOnIce', 'ppTimeOnIce', 'fanPoints', 'points']
team_list = ['goalsAgainst', 'shotsAgainstPerGame']

home_teams, road_teams, games_dict_home, games_dict_road, goalie_dict = today_data.daily(daily_url=daily_url, nhl_teams=nhl_teams, team_map=team_map, road_teams_xpath=road_team_xpath, home_teams_xpath=home_team_xpath, road_goalies_xpath=road_goalie_xpath, home_goalies_xpath= home_goalie_xpath)

df_goalie, df = data.main(goalie=True)

df = today_data.today_df(df=df, home_teams=home_teams, road_teams=road_teams, cutoff="12-01-2022", today=today, games_dict_home=games_dict_home, games_dict_road=games_dict_road, goalie_dict=goalie_dict, df_goalie=df_goalie)

df = data_prep.main(df, goalie_list=goalie_list, skater_list=skater_list, team_list=team_list, per_sixty_list=None)

cat_var = ['homeRoad', 'positionCode', 'shootsCatches']


edf = data_train.ohe(df, cat_vars=cat_var)

features = ['OpHomeDummy', 'OpRoadDummy', 'savePctLastGame', 'savePctMa3', 'savePctMa7','savePctMa16', 'goalsLastGame','goalsMa3', 'goalsMa7', 'goalsMa16', 'shotsLastGame', 'shotsMa3', 'shotsMa7', 'shotsMa16', 'timeOnIceLastGame', 'timeOnIceMa3', 'timeOnIceMa7', 'timeOnIceMa16', 'ppTimeOnIceLastGame','ppTimeOnIceMa3', 'ppTimeOnIceMa7','ppTimeOnIceMa16', 'fanPointsLastGame','fanPointsMa3', 'fanPointsMa7','fanPointsMa16', 'pointsLastGame','pointsMa3', 'pointsMa7','pointsMa16','goalsAgainstLastGame','goalsAgainstMa3','goalsAgainstMa7', 'goalsAgainstMa16', 'shotsAgainstPerGameLastGame','shotsAgainstPerGameMa3', 'shotsAgainstPerGameMa7','shotsAgainstPerGameMa16', '0', '1', '2', '3', '4', '5', '6', '7']

pred_df = edf[edf['gameDate'] == today]

def make_preds(df, model_path, columns, scale=True):
    """
    makes predictions by loading in model and saves predictions to desktop

    params
    ----------------------
    df: dataframe
    model_path: path to model
    columns: columns to display in final prediction csv
    scale: whether to scale the data or not

    returns
    ----------------------
    csv file of predictions to desktop 
    """

    df.columns = df.columns.astype(str)
    X = df[features].values
    

    if scale:
        scaler=RobustScaler()
        X = scaler.fit_transform(X)
    model = joblib.load(model_path)


    predictions = model.predict(X)

    df['predictions'] = predictions


    pred_df = df[columns].sort_values('predictions', ascending=False)


    pred_df.to_csv(f'~/Desktop/pred_{today}.csv')

    
make_preds(df=pred_df, model_path='/Users/nickdimmitt/sportsmodels/nhl/models/fanpoints/skaters/models/fanPoints.pkl', columns= ['skaterFullName', 'teamAbbrevMerge', 'opponentTeamAbbrev', 'predictions'], scale=True)