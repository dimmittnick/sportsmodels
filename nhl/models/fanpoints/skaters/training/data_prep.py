import pandas as pd
import numpy as np

def fan_points(df):
    
    fan_points = ((df['assists'] * 8) + (df['goals'] * 12) + (df['blockedShots'] * 1.6) +(df['ppPoints'] * 0.5) + (df['shots'] * 1.6) + (df['shPoints'] * 2))
    
    return fan_points


def overperform(df, column, groupby):
    
    over_perf = df.groupby(groupby)[column].transform(lambda x: x - x.mean())
    
    return over_perf

def over_perf_dummy(df, column):
    
    new_col  = np.where(df[column] > 0, 1, 0)
    
    return new_col

def under_perf_dummy(df, column):
    
    new_col = np.where(df[column] < 0, 1, 0)
    
    return new_col
    
def same_perf_dummy(df, column):
    
    new_col = np.where(df[column] == 0, 1, 0)

    return new_col

def home_away_perf(df, column, groupby):
    
    home_perf = df.groupby(groupby)[column].transform(lambda x: x.mean())
    
    return home_perf

def stat_per_60(df, time_column, stat_col):
    
    new_col = (df[stat_col] / df[time_column])*360
    
    return new_col

def moving_average(df, column, groupby, window):
    
    ma = df.groupby(groupby)[column].transform(lambda x: x.rolling(window).mean().shift(1))
    
    return ma

def main(df, goalie_list, skater_list, team_list, per_sixty_list):

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

    return df