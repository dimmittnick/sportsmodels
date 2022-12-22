this is the first ml model i made. predicts fantasy points for skaters on daily basis.

target: fantasy points
features:
method:
score:

the first run resulted in an model score of .58 and it placed feature importance on good variables opponent and fanpoitns ma16. very very happy with this result.

features: ['OpHomeDummy', 'OpRoadDummy', 'savePctLastGame', 'savePctMa3', 'savePctMa7','savePctMa16', 'goalsLastGame','goalsMa3', 'goalsMa7', 'goalsMa16', 'shotsLastGame', 'shotsMa3', 'shotsMa7', 'shotsMa16', 'timeOnIceLastGame', 'timeOnIceMa3', 'timeOnIceMa7', 'timeOnIceMa16', 'ppTimeOnIceLastGame','ppTimeOnIceMa3', 'ppTimeOnIceMa7','ppTimeOnIceMa16', 'fanPointsLastGame','fanPointsMa3', 'fanPointsMa7','fanPointsMa16', 'pointsLastGame','pointsMa3', 'pointsMa7','pointsMa16','goalsAgainstLastGame','goalsAgainstMa3','goalsAgainstMa7', 'goalsAgainstMa16', 'shotsAgainstPerGameLastGame','shotsAgainstPerGameMa3', 'shotsAgainstPerGameMa7','shotsAgainstPerGameMa16', '0', '1', '2', '3', '4', '5', '6', '7']


target: 'fanPoints'

mean absolute error: 3.8333463047623084
model score: 0.5812866782086444
OpHomeDummy: 0.0029866157565265894
OpRoadDummy: 0.018474502488970757
savePctLastGame: 0.0170621108263731
savePctMa3: 0.015913136303424835
savePctMa7: 0.016936354339122772
savePctMa16: 0.010333838872611523
goalsLastGame: 0.005917485803365707
goalsMa3: 0.0066689420491456985
goalsMa7: 0.006232311949133873
goalsMa16: 0.00674346461892128
shotsLastGame: 0.005267447326332331
shotsMa3: 0.006605417001992464
shotsMa7: 0.008621969260275364
shotsMa16: 0.013321274891495705
timeOnIceLastGame: 0.008907529525458813
timeOnIceMa3: 0.01170834805816412
timeOnIceMa7: 0.007213190197944641
timeOnIceMa16: 0.0068052695132792
ppTimeOnIceLastGame: 0.012989528477191925
ppTimeOnIceMa3: 0.01621530018746853
ppTimeOnIceMa7: 0.014289465732872486
ppTimeOnIceMa16: 0.010876580141484737
fanPointsLastGame: 0.035634852945804596
fanPointsMa3: 0.01520776841789484
fanPointsMa7: 0.029400963336229324
fanPointsMa16: 0.0914868637919426
pointsLastGame: 0.029320143163204193
pointsMa3: 0.008630255237221718
pointsMa7: 0.011072919704020023
pointsMa16: 0.011835435405373573
goalsAgainstLastGame: 0.0713731199502945
goalsAgainstMa3: 0.15466459095478058
goalsAgainstMa7: 0.1276976615190506
goalsAgainstMa16: 0.028528859838843346
shotsAgainstPerGameLastGame: 0.03330659866333008

learning rate = 0.1
estimators = 1500
max_depth = 5
