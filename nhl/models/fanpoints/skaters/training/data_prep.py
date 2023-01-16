import pandas as pd
import numpy as np

def fan_points(df):
    """
    calculates fanduel fantasy point for each skater by game

    params
    ----------------------
    df: dataframe containing game by game and skater by skater data

    returns
    ----------------------
    fan_points: series containing the fanpoints column
    """
    
    fan_points = ((df['assists'] * 8) + (df['goals'] * 12) + (df['blockedShots'] * 1.6) +(df['ppPoints'] * 0.5) + (df['shots'] * 1.6) + (df['shPoints'] * 2))
    
    return fan_points


def overperform(df, column, groupby):
    """
    calculates overperform column for each skater by game

    params
    ----------------------
    df: dataframe containing game by game and skater by skater data
    column: column to test overperformance
    groupby: column to group by

    returns
    ----------------------
    over_perf: series containing the over_performance column
    """
    
    over_perf = df.groupby(groupby)[column].transform(lambda x: x - x.mean())
    
    return over_perf

def over_perf_dummy(df, column):
    """
    calculates overperformance dummy variable

    params
    ----------------------
    df: dataframe containing game by game and skater by skater data
    column: column to create dummy variable off of

    returns
    ----------------------
    new_col: dummy column containing 1's where player overperformed and 0 where they didnt
    """
    
    new_col  = np.where(df[column] > 0, 1, 0)
    
    return new_col

def under_perf_dummy(df, column):
    """
    calculates underperformance dummy variable

    params
    ----------------------
    df: dataframe containing game by game and skater by skater data
    column: column to create dummy variable off of

    returns
    ----------------------
    new_col: dummy column containing 1's where player underperformed and 0 where they didnt
    """
    
    new_col = np.where(df[column] < 0, 1, 0)
    
    return new_col
    
def same_perf_dummy(df, column):
    """
    calculates same performance dummy variable

    params
    ----------------------
    df: dataframe containing game by game and skater by skater data
    column: column to create dummy variable off of

    returns
    ----------------------
    new_col: dummy column containing 1's where player performs the same and 0 where they didnt
    """
    
    new_col = np.where(df[column] == 0, 1, 0)

    return new_col

def home_away_perf(df, column, groupby):
    """
    calculates average fan points for home away splits per player

    params
    ----------------------
    df: dataframe containing game by game and skater by skater data
    column: column to create dummy variable off of

    returns
    ----------------------
    new_col: dummy column containing 1's where player performs the same and 0 where they didnt
    """
    
    home_perf = df.groupby(groupby)[column].transform(lambda x: x.mean())
    
    return home_perf

def stat_per_60(df, time_column, stat_col):
    """
    calculates stats per 60 minutes toi per player per game

    params
    ----------------------
    df: dataframe
    time_column: toi columns
    stat_col: column containing statistic

    returns
    ----------------------
    new_col: series containing new statistic
    """
    
    new_col = (df[stat_col] / df[time_column])*360
    
    return new_col

def moving_average(df, column, groupby, window):
    """
    calcualtes moving average for statistics

    params
    ----------------------
    df: datafame
    column: stat clumns
    groupby: how to group data and calculate moving average
    window: moving average number

    returns
    ----------------------
    ma: series containing moving average data
    """
    
    ma = df.groupby(groupby)[column].transform(lambda x: x.rolling(window).mean().shift(1))
    
    return ma

def main(df, goalie_list, skater_list, team_list, per_sixty_list):
    """
    main function

    params
    ----------------------
    df: datafame
    goalie_list: list of goalie stats to be prepped
    skater_list: list of skater stat columns to be prepped
    team_list: list of team stat columns to be prepped
    per_sixty_list: list of stat columns for per 60 calculations

    returns
    ----------------------
    dataframe: dataframe containing prepped data
    """

    df['fanPoints'] = fan_points(df=df)
    df['overPerform'] = overperform(df=df, column='fanPoints', groupby='playerId')
    df['homeRoadPerf'] = home_away_perf(df=df, column='overPerform', groupby=['playerId', 'homeRoad'])
    
    better_home_skater = list(np.where((df['homeRoad'] == 'H') & (df['homeRoadPerf'] > 0), df['playerId'], None))
    better_away_skater = list(np.where((df['homeRoad'] == 'R') & (df['homeRoadPerf'] > 0), df['playerId'], None))
    better_home_skater = [*set(better_home_skater)]
    better_away_skater = [*set(better_away_skater)]

    df['OpHomeDummy'] = np.where(df['playerId'].isin(better_home_skater), 1, 0)
    df['OpRoadDummy'] = np.where(df['playerId'].isin(better_away_skater), 1, 0)
    df['OpNowhereDummy'] = np.where((df['OpHomeDummy'] == 0) & (df['OpRoadDummy'] == 0), 1, 0)

    df.sort_values('gameDate', ascending=True, inplace=True)

    for x in goalie_list:
        df[f'{x}LastGame'] = moving_average(df=df, column=x, groupby='goalieId', window=1)
        df[f'{x}Ma3'] = moving_average(df=df, column=x, groupby='goalieId', window=3)
        df[f'{x}Ma7'] = moving_average(df=df, column=x, groupby='goalieId', window=7)
        df[f'{x}Ma16'] = moving_average(df=df, column=x, groupby='goalieId', window=16)
    
    for x in skater_list:
        df[f'{x}LastGame'] = moving_average(df=df, column=x, groupby='playerId', window=1)
        df[f'{x}Ma3'] = moving_average(df=df, column=x, groupby='playerId', window=3)
        df[f'{x}Ma7'] = moving_average(df=df, column=x, groupby='playerId', window=7)
        df[f'{x}Ma16'] = moving_average(df=df, column=x, groupby='playerId', window=16)
    
    for x in team_list:
        df[f'{x}LastGame'] = moving_average(df=df, column=x, groupby='opponentTeamAbbrev', window=1)
        df[f'{x}Ma3'] = moving_average(df=df, column=x, groupby='opponentTeamAbbrev', window=3)
        df[f'{x}Ma7'] = moving_average(df=df, column=x, groupby='opponentTeamAbbrev', window=7)
        df[f'{x}Ma16'] = moving_average(df=df, column=x, groupby='opponentTeamAbbrev', window=16)

    df.drop_duplicates(inplace=True)
    df = df[df['fanPointsMa16'] > 6]

    return df