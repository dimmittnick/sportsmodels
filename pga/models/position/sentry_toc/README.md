sentry tournament of champions model

only have very basic dataset for this model

plan is to continue to exapnd on data and feature week after week to narrow down best model for each tournament

score: 0.19713071547096506
features: ['sg_puttLastTour', 'sg_puttMa3', 'sg_puttMa7',
       'sg_puttMa21', 'sg_argLastTour', 'sg_argMa3', 'sg_argMa7', 'sg_argMa21',
       'sg_appLastTour', 'sg_appMa3', 'sg_appMa7', 'sg_appMa21',
       'sg_ottLastTour', 'sg_ottMa3', 'sg_ottMa7', 'sg_ottMa21',
       'sg_t2gLastTour', 'sg_t2gMa3', 'sg_t2gMa7', 'sg_t2gMa21',
       'sg_totalLastTour', 'sg_totalMa3', 'sg_totalMa7', 'sg_totalMa21', 'lastyear_pos', 'last3_pos', 'last5_pos']

feature importances:

sg_puttLastTour:0.015394287183880806
sg_puttMa3:0.02313988469541073
sg_puttMa7:0.023344775661826134
sg_puttMa21:0.017286866903305054
sg_argLastTour:0.02855425700545311
sg_argMa3:0.06560413539409637
sg_argMa7:0.07259376347064972
sg_argMa21:0.018146488815546036
sg_appLastTour:0.0483953021466732
sg_appMa3:0.041841838508844376
sg_appMa7:0.04242013767361641
sg_appMa21:0.036534931510686874
sg_ottLastTour:0.031664181500673294
sg_ottMa3:0.036101534962654114
sg_ottMa7:0.03445819392800331
sg_ottMa21:0.02560112625360489
sg_t2gLastTour:0.044387683272361755
sg_t2gMa3:0.038627345114946365
sg_t2gMa7:0.060425207018852234
sg_t2gMa21:0.03919120505452156
sg_totalLastTour:0.02521505579352379
sg_totalMa3:0.056819163262844086
sg_totalMa7:0.048279646784067154
sg_totalMa21:0.03989614546298981
lastyear_pos:0.025668488815426826
last3_pos:0.06040830537676811
last5_pos:0.0

im very happy with this as a baseline model. can make this in 10 minutes for any tournament. looking to add in more categorical variables such as course features (weather, grass, slope, distance). maybe even make models for individual courses, dont know if there is enough data on it. want to include player information also, age, handedness, drive distance, preferred shot type, etc. maybe some more tangible statistics as well.

model = xgb.XGBRegressor(learning_rate = 0.009, n_estimators=350, max_depth=3, min_split_loss=0, reg_lambda=1, reg_alpha=2, colsample_bylevel=0, colsample_bytree=1, max_delta_step=0)