sentry tournament of champions model

only have very basic dataset for this model

plan is to continue to exapnd on data and feature week after week to narrow down best model for each tournament

score: 0.16145456649142076
features: ['sg_puttMa3', 'sg_puttMa7', 'sg_puttMa21', 'sg_argMa3',
       'sg_argMa7', 'sg_argMa21', 'sg_appMa3', 'sg_appMa7', 'sg_appMa21',
       'sg_ottMa3', 'sg_ottMa7', 'sg_ottMa21', 'sg_t2gMa3', 'sg_t2gMa7',
       'sg_t2gMa21', 'sg_totalMa3', 'sg_totalMa7', 'sg_totalMa21']

feature importances:

sg_puttMa3:0.025264138355851173
sg_puttMa7:0.025778712704777718
sg_puttMa21:0.016408849507570267
sg_argMa3:0.029802698642015457
sg_argMa7:0.11537399888038635
sg_argMa21:0.010738903656601906
sg_appMa3:0.021029705181717873
sg_appMa7:0.01941688358783722
sg_appMa21:0.032372504472732544
sg_ottMa3:0.022446569055318832
sg_ottMa7:0.021441303193569183
sg_ottMa21:0.04770486056804657
sg_t2gMa3:0.03380376845598221
sg_t2gMa7:0.18807007372379303
sg_t2gMa21:0.045182954519987106
sg_totalMa3:0.1445164829492569
sg_totalMa7:0.11653167754411697
sg_totalMa21:0.0841159075498581

im very happy with this as a baseline model. can make this in 10 minutes for any tournament. looking to add in more categorical variables such as course features (weather, grass, slope, distance). maybe even make models for individual courses, dont know if there is enough data on it. want to include player information also, age, handedness, drive distance, preferred shot type, etc. maybe some more tangible statistics as well.

Justin Thomas	     6.044477
Keegan Bradley	     7.905571
Scottie Scheffler	 8.130801
Matthew Fitzpatrick	 8.220900
Aaron Wise	         8.442068
Hideki Matsuyama	 8.574217
Xander Schauffele	 8.940044
Collin Morikawa	     9.419708
Corey Conners	     10.312182
Sungjae Im	         10.331885
Jordan Spieth	     13.117905
Cameron Young	     14.161210
Tony Finau	         14.803812
Billy Horschel	     14.970281
Will Zalatoris	     15.733332
Russell Henley	     15.913927
Jon Rahm	         16.292511
Patrick Cantlay	     17.744057
Seamus Power	     20.260010
Brian Harman	     20.789623
Kyoung-Hoon Lee	     21.541763
Max Homa	         21.697989
Trey Mullinax	     22.393137
Adam Svensson	     22.466478
Sahith Theegala	     22.758749
Sepp Straka	         22.983480
Sam Burns	         23.044899
Tom Hoge	         23.120253
Viktor Hovland	     23.699663
J.J. Spaun	         24.192608
Mackenzie Hughes	 26.712814
Scott Stallings	     28.334127
Chez Reavie	         29.540133
J.T. Poston	         29.679117
Joohyung Kim	     29.778200
Adam Scott	         30.177465
Luke List	         32.961262
Ryan Brehm	         34.274281

