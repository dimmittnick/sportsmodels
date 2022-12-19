import mysql
import mysql.connector
from mysql.connector import errorcode

## obtain connection string information from portal
config = {
    "host":"nhlserver.mysql.database.azure.com",
    "user":"nicholasdimmitt",
    "password":"1999Dexter$$",
    "database":"daily"
}

# construct connection string

try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

# create table
cursor.execute("CREATE TABLE skaters(assists INT, ev_goals INT, ev_points INT, faceoff_win_pct FLOAT, game_date DATE, game_id INT, game_winning_goals INT, games_played INT, goals INT, home_road CHAR, last_name VARCHAR(24), opponent_team_abbrev VARCHAR(5), ot_goals INT, penalty_minutes INT, player_id INT, plus_minus INT, points INT, points_per_game FLOAT, position_code CHAR, pp_goals INT, pp_points INT, sh_goals INT, sh_points INT, shooting_pct FLOAT, shoots_catches CHAR, shots INT, skater_full_name VARCHAR(64), team_abbrev VARCHAR(3), toi FLOAT)")


# cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")