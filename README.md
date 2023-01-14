# sportsmodels

Repository for sportsmodels.org. This website will leverage machine learning and datasets that update daily to allow users to construct their own ML models and create daily predictions to support them in fantasy, sports betting, or pure interest. Will give use the ability to select their target variable and what features they want to use then will spit out daily predictions. Will eventually scale into all sports and longer time frames that don't necesarilly do daily predictions. The first model is an nhl daily predictions model.


12-16-2022

Need to get familiar with microsoft azure to house the data. Need to create a way that will update the database everyday. have the code to do it but dont know the link between the database and bulk uploading csv files.

12-19-2022

Slightly discouraged today. Started research on training ml models in web applications and there is A LOT to it. Nonetheless noticing a couple errors in my nhl fanpoints model that was skewing the predictions. Also tried to set up database for nhl data and failed epically. Will just start with a simple sqlite database because AWS, azure, and postgress were pissing me off. Building out the structure for this repo, will have multiple models that make daily predictions and then build from there. start small and scale up to interactive ML building on the website.

1-14-2023

have made decent process for pga models, more importantly have started developing the bones for sportsmodels.com. Will have multiple pages for mlb, nhl, pga predictions where manually running modle with populate database which will update on the webpage. very limited interactivity for the user but having a platform for the models is an important first step. 
