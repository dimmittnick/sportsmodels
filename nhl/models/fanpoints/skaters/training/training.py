import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import xgboost as xgb

def ohe(df, cat_vars):
    '''function that handles categorical variables with one hot encoder

    attributes
    ----------------------
    df: dataframe containing categorical and numerical features
    cat_vars: list of column names containing cateforical variables

    returns
    ----------------------
    encode_df: dataframe containing one hot encoded variables
    '''
    encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
    encode_cols = pd.DataFrame(encoder.fit_transform(df[cat_vars]))
    encode_cols.index = df.index

    numer_df = df.drop(cat_vars, axis=1)

    encode_df = pd.concat([numer_df, encode_cols], axis=1)

    return encode_df

def trainer(df, features, target, learning_rate, n_estimators, max_depth, scale=True, save_model=False):
    '''function to trains model

    attributes
    ----------------------
    df: dataframe containing features and target variable
    features: list of column names containing features
    target: column name of target variable
    learning_rate: learning rate of xgboost model, default is 0.1
    n_estimators: number of trees, default is 1000
    max_depth: maximum number of splits per tree, default is 4
    scale: whether to scale features or not


    returns
    ----------------------
    mean absolute error and model score based off test data
    '''

    X = df[features].values
    X.columns = X.columns.astype(str)

    y = df[target].values

    if scale:
        scaler=RobustScaler()
        X = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=342)
    model = xgb.XGBRegressor(learning_rate=learning_rate, n_estimators=n_estimators, max_depth=max_depth)
    model.fit(X_train, y_train, early_stopping_rounds=5, eval_metric='mae', eval_set=[(X_train, y_train)], verbose=False)

    print(f"mean absolute error: {mean_absolute_error(model.predict(X_test), y_test)}")
    print(f"model score: {model.score(X_test, y_test)}")

    for x,y in zip(features, model.feature_importances_):
        print(f"{x}: {y}")

    if save_model:
        joblib.dump(model, f"~/sportsmodels/nhl/models/fanpoints/skaters/models/{target}.pkl")
    




