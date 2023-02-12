import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")
    else:
        print(err)
    
#create cursor
cursor = db.cursor()

update = """
INSERT INTO player (first_name, last_name, team_id)
VALUES('Smeagol', 'Shire Folk', 1);
"""
second_query = """ 
SELECT player_id, first_name, last_name, team_name
FROM player
INNER JOIN team
ON player.team_id = team.team_id;
"""
cursor.execute(update)
cursor.execute(second_query)

players = cursor.fetchall()

print("-- DISPLAYING PLAYER AFTER INSERT --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print("\n")

update_query = """
UPDATE player
SET team_id = 2,
    first_name = 'Gollum',
    last_name = 'Ring Stealer'
WHERE first_name = 'Smeagol';
"""

cursor.execute(update_query)
cursor.execute(second_query)
players = cursor.fetchall()

print("-- DISPLAYING PLAYER AFTER UPDATE --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print("\n")


delete_query = """
DELETE FROM player
WHERE first_name = 'Gollum';
"""
cursor.execute(delete_query)
cursor.execute(second_query)

players = cursor.fetchall()
print("-- DISPLAYING PLAYER AFTER DELETE --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print("\n")