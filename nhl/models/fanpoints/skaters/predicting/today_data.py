import pandas as pd
import numpy as np
import joblib
from lxml import etree, html
from datetime import *
from dateutil import relativedelta
import requests
import json
htmlparser = etree.HTMLParser()

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

def daily(daily_url, nhl_teams, team_map, road_teams_xpath, home_teams_xpath, road_goalies_xpath, home_goalies_xpath):
    """
    scraps and returns all of the daily matchups and goalies 

    params
    ----------------------
    daily_url: rotowire url to todays games
    nhl_teams: list of all nhl team abbrevs
    team_map: mapping of rotowire abbrev to nhl abbrev
    road_teams_xpath: xpath to grab all road teams
    home_teams_xpath: xpath to grab all home teams
    road_goalies_xpath: xpath to grab all road goalies
    home_goalies_xapth: xpath to grab all home goalies

    returns
    ----------------------
    home_teams: list of home team abbrevs
    road_teams: list of road team abbrevs
    games_dict_home: dictionary containing home teams as key and road teams as value
    games_dict_road: dictionary containg road teams as key and home teams as value
    goalie_dict: dictionary containing team abbrev as key and opposing goalie as value
    """
    results = requests.get(daily_url)
    results_tree = html.fromstring(results.content)

    road_teams = results_tree.xpath(road_teams_xpath)
    home_teams = results_tree.xpath(home_teams_xpath)

    road_teams = [team_map[x] for x in road_teams if x in nhl_teams]
    home_teams = [team_map[x] for x in home_teams if x in nhl_teams]

    games_road = [(x,y) for x,y in zip(road_teams, home_teams)]
    games_home = [(x,y) for x,y in zip(home_teams, road_teams)]

    games_dict_road = dict(games_road)
    games_dict_home = dict(games_home)

    home_goalies = results_tree.xpath(home_goalies_xpath)
    road_goalies = results_tree.xpath(road_goalies_xpath)

    goalie_dict = {}
    for x in range(len(home_goalies)):
        goalie_dict[road_teams[x]] = home_goalies[x]
        goalie_dict[home_teams[x]] = road_goalies[x]
    
    return home_teams, road_teams, games_dict_home, games_dict_road, goalie_dict

    
def today_df(df, home_teams, road_teams, cutoff, today, games_dict_home, games_dict_road, goalie_dict, df_goalie):
    """
    adds daily data to the entire data frame to make it ready for modeling

    params
    ----------------------
    df: dataframe
    home_teams: list of todays home teams
    road_teams: list of todays road teams
    cutoff: cutoff date for data grab
    today: todays date
    games_dict_home: dictionary containing home teams as key and road teams as value
    games_dict_road: dictionary containg road teams as key and home teams as value
    goalie_dict: dictionary containing team abbrev as key and opposing goalie as value

    returns
    ----------------------
    dataframe: dataframe containing todays data
    """
    
    today_home_df = df[(df['gameDate'] > cutoff) & (df['teamAbbrevMerge'].isin(home_teams))]
    today_road_df = df[(df['gameDate'] > cutoff) & (df['teamAbbrevMerge'].isin(road_teams))]


    today_home_df['gameDate'] = today
    today_road_df['gameDate'] = today

    today_home_df['homeRoad'] = 'H'
    today_road_df['homeRoad'] = 'R'

    today_home_df[['goals', 'assists',
       'plusMinus', 'points', 'ppGoals', 'ppPoints', 'shGoals',
       'shPoints', 'shootingPct', 'shots', 'blockedShots', 'ppTimeOnIce', 'shTimeOnIce', 'shifts', 'timeOnIce',
       'timeOnIcePerShift', 'savePct', 'goalsAgainst', 'shotsAgainstPerGame']] = 0

    today_road_df[['goals', 'assists',
       'plusMinus', 'points', 'ppGoals', 'ppPoints', 'shGoals',
       'shPoints', 'shootingPct', 'shots', 'blockedShots', 'ppTimeOnIce', 'shTimeOnIce', 'shifts', 'timeOnIce',
       'timeOnIcePerShift', 'savePct', 'goalsAgainst', 'shotsAgainstPerGame']] = 0
    
    today_road_df['opponentTeamAbbrev'] = today_road_df['teamAbbrevMerge'].map(games_dict_road)
    today_home_df['opponentTeamAbbrev'] = today_home_df['teamAbbrevMerge'].map(games_dict_home)


    today_road_df['goalieFullName'] = today_road_df['teamAbbrevMerge'].map(goalie_dict)
    today_home_df['goalieFullName'] = today_home_df['teamAbbrevMerge'].map(goalie_dict)

    today_df = pd.concat([today_home_df, today_road_df])
    today_df.drop_duplicates(subset='playerId', keep='last', inplace=True)

    goalies = list(df_goalie['goalieFullName'])
    goalieId = list(df_goalie['goalieId'])

    goalie_map = {}

    for i in range(len(goalies)):
        goalie_map[goalies[i]] = goalieId[i]

    today_df['goalieId'] = today_df['goalieFullName'].map(goalie_map)

    today_df['gameDate'] = today

    df = pd.concat([df, today_df])
    
    return df