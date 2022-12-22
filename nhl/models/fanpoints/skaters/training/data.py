import pandas as pd
import numpy as np
import json
import requests
from datetime import *
from dateutil import relativedelta

## this needs to be updated after data is read in everytime and added to database
## most recent date: 11/01/22
end_date = "2022-11-30"
yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
today = datetime.today().strftime("%Y-%m-%d")

def webscrape(url, data_string):
    """
    takes in nhl.com/stats api url and returns data based off dates and page number

    params
    ----------------------
    url: nhl.api url
    data_string: string that takes you to json data from url

    returns
    ----------------------
    dataframe: dataframe containing scraped data
    """
    try:
        response = requests.get(url).text
        data = json.loads(response)
        
        return pd.DataFrame(data[data_string])
    
    except:
        return print(f'URL Error: {url}')
    

def url_gen(start_date, end_date, page, data_seg):
    """
    generates url to webscrape from depending on date range that use inputs

    params
    ----------------------
    start date: date you want to start webscraping from
    end_date: usually yesterday, up to what date you want to webscrape from
    page: the specific page in webpage to scrape from, this is automatically filled in main()

    returns
    ----------------------
    url: url to scrape from
    """
    
    skater_url = f'https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=true&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22playerId%22,%22direction%22:%22ASC%22%7D%5D&start={page}&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameDate%3C=%22{end_date}%2023%3A59%3A59%22%20and%20gameDate%3E=%22{start_date}%22%20and%20gameTypeId=2'
    
    misc_url = f'https://api.nhle.com/stats/rest/en/skater/realtime?isAggregate=false&isGame=true&sort=%5B%7B%22property%22:%22hits%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22playerId%22,%22direction%22:%22ASC%22%7D%5D&start={page}&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameDate%3C=%22{end_date}%2023%3A59%3A59%22%20and%20gameDate%3E=%22{start_date}%22%20and%20gameTypeId=2'                                
    
    shots_url = f'https://api.nhle.com/stats/rest/en/skater/shottype?isAggregate=false&isGame=true&sort=%5B%7B%22property%22:%22shots%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22shootingPct%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22playerId%22,%22direction%22:%22ASC%22%7D%5D&start={page}&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameDate%3C=%22{end_date}%2023%3A59%3A59%22%20and%20gameDate%3E=%22{start_date}%22%20and%20gameTypeId=2'
    
    per_sixty_url = f'https://api.nhle.com/stats/rest/en/skater/scoringpergame?isAggregate=false&isGame=true&sort=%5B%7B%22property%22:%22pointsPerGame%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goalsPerGame%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22playerId%22,%22direction%22:%22ASC%22%7D%5D&start={page}&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameDate%3C=%22{end_date}%2023%3A59%3A59%22%20and%20gameDate%3E=%22{start_date}%22%20and%20gameTypeId=2'
    
    toi_url = f'https://api.nhle.com/stats/rest/en/skater/timeonice?isAggregate=false&isGame=true&sort=%5B%7B%22property%22:%22timeOnIce%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22playerId%22,%22direction%22:%22ASC%22%7D%5D&start={page}&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameDate%3C=%22{end_date}%2023%3A59%3A59%22%20and%20gameDate%3E=%22{start_date}%22%20and%20gameTypeId=2'
    
    goalie_url = f'https://api.nhle.com/stats/rest/en/goalie/summary?isAggregate=false&isGame=true&sort=%5B%7B%22property%22:%22wins%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22savePct%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22playerId%22,%22direction%22:%22ASC%22%7D%5D&start={page}&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameDate%3C=%22{end_date}%2023%3A59%3A59%22%20and%20gameDate%3E=%22{start_date}%22%20and%20gameTypeId=2'
    
    team_url = f'https://api.nhle.com/stats/rest/en/team/summary?isAggregate=false&isGame=true&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22wins%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22teamId%22,%22direction%22:%22ASC%22%7D%5D&start={page}&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameDate%3C=%22{end_date}%2023%3A59%3A59%22%20and%20gameDate%3E=%22{start_date}%22%20and%20gameTypeId=2'
    
    if data_seg == 'skater':
        return skater_url
    
    elif data_seg == 'misc':
        return misc_url
    
    elif data_seg == 'shots':
        return shots_url
    
    elif data_seg == 'scor':
        return per_sixty_url
    
    elif data_seg == 'toi':
        return toi_url
    
    elif data_seg == 'goal':
        return goalie_url
    
    else:
        return team_url


def date_list_gen(start, end):
    """
    generates the dates by month 

    params
    ----------------------
    start: date to start from
    end: date to end

    returns
    ----------------------
    returns list of dates from start to end
    """
    
    start_date = datetime.strptime(start, '%Y-%m-%d').date()
    end_date = datetime.strptime(end, '%Y-%m-%d').date()
    current_date = start_date
    date_list = []
    
    while current_date > end_date:
        last_month = current_date - relativedelta.relativedelta(months=1)
        tup = (str(current_date), str(last_month))
        date_list.append(tup)
        current_date = last_month
    
    return date_list



def df_gen(start_date, end_date, data_seg, update_path, start, stop, step, update=False, save_data=False):
    """
    generates dataframe 

    params
    ----------------------
    start_date: date to start webscraping from
    end_date: date to end scraping
    data_seg: string that specifies data segment
    update_path: path to data that has already been generated, ideally would be a database but can be a path to a csv files
    start: page to start at
    stop: page to stop at, page number of 10000th term ideally
    step: what to increment the pages by
    update: whether to use the old data also
    save_data: whether to overwrite the old data with the updated data

    returns
    ----------------------
    dataframe: dataframe containing updated dataframe with modeling data
    """
    if update:
        df_old = pd.read_csv(update_path)
        
    date_list = date_list_gen(start_date, end_date)
    
    df_list = [[webscrape(url_gen(y[1], y[0], x, data_seg), 'data') for y in date_list] for x in range(start, stop, step)]
    
    df_list_flat = [df for sublist in df_list for df in sublist]

    df = pd.concat(df_list_flat)
    
    if update:
        df_update = pd.concat([df, df_old])
    
    if save_data:
        df_update.to_csv(f"/Users/nickdimmitt/Desktop/dfs_locally/df_{data_seg}.csv")
    
    if update:
        
        return df_update
    
    return df




def main(goalie=False):
    """main function that creates single dataframe for modeling and feature engineering with all the data segments

    params
    ----------------------

    returns
    ----------------------
    dataframe: clean dataframe containing all data segments ready for feature engineering and modeling
    """

    df_skater = df_gen(start_date=yesterday, end_date=end_date, data_seg='skater', update_path="/Users/nickdimmitt/Desktop/dfs_local/data/skaters.csv", start=0, stop=10000, step=100, update=True, save_data=False)
    df_misc = df_gen(start_date=yesterday, end_date=end_date, data_seg='misc', update_path="/Users/nickdimmitt/Desktop/dfs_local/data/misc.csv", start=0, stop=10000, step=100, update=True, save_data=False)
    df_shot = df_gen(start_date=yesterday, end_date=end_date, data_seg='shots', update_path="/Users/nickdimmitt/Desktop/dfs_local/data/shots.csv", start=0, stop=10000, step=100, update=True, save_data=False)
    df_toi = df_gen(start_date=yesterday, end_date=end_date, data_seg='toi', update_path="/Users/nickdimmitt/Desktop/dfs_local/data/toi.csv", start=0, stop=10000, step=100, update=True, save_data=False)
    df_goalie = df_gen(start_date=yesterday, end_date=end_date, data_seg='goalie', update_path="/Users/nickdimmitt/Desktop/dfs_local/data/goalies.csv", start=0, stop=10000, step=100, update=True, save_data=False)
    df_team = df_gen(start_date=yesterday, end_date=end_date, data_seg='team', update_path="/Users/nickdimmitt/Desktop/dfs_local/data/teams.csv", start=0, stop=10000, step=100, update=True, save_data=False)

    df_skater = df_skater.drop(['evGoals', 'evPoints','faceoffWinPct', 'gameWinningGoals', 'gamesPlayed', 'lastName', 'otGoals', 'pointsPerGame', 'timeOnIcePerGame'], axis=1)
    df_skater = df_skater.loc[:, ~df_skater.columns.str.contains('^Unnamed')]
    df_skater['teamAbbrevMerge'] = df_skater['teamAbbrev'].copy()

    df_misc = df_misc.drop(['blockedShotsPer60', 'emptyNetAssists', 'homeRoad', 'emptyNetGoals', 'emptyNetPoints', 'firstGoals', 'gamesPlayed', 'giveaways', 'giveawaysPer60', 'hits', 'hitsPer60', 'missedShotCrossbar', 'missedShotGoalpost', 'missedShotOverNet', 'missedShotWideOfNet', 'missedShots', 'opponentTeamAbbrev', 'otGoals', 'takeaways', 'takeawaysPer60'], axis=1)
    df_misc = df_misc.loc[:, ~df_misc.columns.str.contains('^Unnamed')]

    df_shot = df_shot.drop(['gamesPlayed', 'goals', 'homeRoad', 'lastName', 'opponentTeamAbbrev', 'teamAbbrev', 'skaterFullName'], axis=1)
    df_shot = df_shot.loc[:, ~df_shot.columns.str.contains('^Unnamed')]

    df_toi = df_toi.drop(['evTimeOnIce', 'evTimeOnIcePerGame', 'gameDate', 'gamesPlayed', 'homeRoad', 'lastName', 'opponentTeamAbbrev','otTimeOnIce', 'otTimeOnIcePerOtGame', 'positionCode', 'shootsCatches','skaterFullName', 'teamAbbrev', 'timeOnIcePerGame'], axis=1)
    df_toi = df_toi.loc[:, ~df_toi.columns.str.contains('^Unnamed')]

    df_goalie = df_goalie.drop(['assists', 'gamesStarted', 'goals', 'goalsAgainstAverage', 'lastName', 'points', 'saves', 'ties', 'timeOnIce', 'wins'], axis=1)
    df_goalie = df_goalie.loc[:, ~df_goalie.columns.str.contains('^Unnamed')]
    df_goalie['goalieId'] = df_goalie['playerId'].copy()
    df_goalie['teamAbbrevMerge'] = df_goalie['opponentTeamAbbrev'].copy()

    df_team = df_team.drop(['faceoffWinPct', 'gamesPlayed', 'goalsAgainstPerGame', 'goalsForPerGame', 'losses', 'otLosses', 'penaltyKillNetPct', 'pointPct', 'powerPlayNetPct', 'powerPlayPct', 'regulationAndOtWins', 'ties', 'wins', 'winsInRegulation', 'winsInShootout'], axis=1)
    df_team = df_team.loc[:, ~df_team.columns.str.contains('^Unnamed')]
    df_team['teamAbbrevMerge'] = df_team['opponentTeamAbbrev'].copy()

    df_goalie = df_goalie[['gameId', 'goalieId','goalieFullName','teamAbbrevMerge','savePct']]
    df_team = df_team[['gameId', 'teamId', 'teamAbbrevMerge', 'goalsAgainst', 'shotsAgainstPerGame']]

    df_merged = pd.merge(df_skater, df_misc, on=['gameId', 'playerId'])
    df_merged.drop_duplicates(inplace=True)

    df_merged = pd.merge(df_merged, df_shot, on=['gameId', 'playerId'])
    df_merged.drop_duplicates(inplace=True)

    df_merged = pd.merge(df_merged, df_toi, on=['gameId', 'playerId'])
    df_merged.drop_duplicates(inplace=True)

    df_merged = pd.merge(df_merged, df_goalie, on=['gameId', 'teamAbbrevMerge'])
    df_merged.drop_duplicates(inplace=True)

    df_merged = pd.merge(df_merged, df_team, on=['gameId', 'teamAbbrevMerge'])
    df_merged.drop_duplicates(inplace=True)

    df_merged = df_merged[['gameId', 'gameDate','playerId', 'opponentTeamAbbrev', 'teamAbbrevMerge', 'homeRoad', 'goalieId', 'goalieFullName', 'goals', 'assists', 'plusMinus',
       'points', 'positionCode_x', 'ppGoals', 'ppPoints', 'shGoals',
       'shPoints', 'shootingPct_x', 'shootsCatches_x', 'shots_x',
       'skaterFullName_x', 'blockedShots',
       'ppTimeOnIce', 'shTimeOnIce', 'shifts', 'timeOnIce',
       'timeOnIcePerShift', 'savePct', 'goalsAgainst', 'shotsAgainstPerGame']]
    
    df_merged.columns = df_merged.columns.str.rstrip('_x')

    if goalie:
        return df_goalie, df_merged
    
    else:
        return df_merged
    

