import sqlite3
from haversine import haversine

db_filename = 'database/srn.db'

global db_conn
global cursor


def init_db():
    global db_conn
    db_conn = sqlite3.connect(db_filename)
    global cursor
    cursor = db_conn.cursor()
    cursor.execute('''CREATE TABLE SRN
             (REAL latitude, REAL longitude, INT severity);''')
    cursor.execute('''USE database_name;''')


# function to add stranger to database
def report_stranger(lat, long, severity=1):
    global cursor
    cursor.execute("INSERT INTO SRN (?,?,?);", lat, long, severity)
    return


def send_closest_srn(lat_user, long_user):
    global cursor
    table = cursor.fetchall()
    return_array = []
    for row in table:
        if haversine((row[0],row[1]), (lat_user, long_user), unit="mi") < 5:
            return_array.append({"lat": row[0], "long": row[1]})

    return return_array

