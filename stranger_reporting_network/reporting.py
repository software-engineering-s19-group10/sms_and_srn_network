import sqlite3
from haversine import haversine
import dateutil.parser as dt_parser
import datetime


db_filename = 'database/srn.db'

global db_conn
global cursor


def init_db():
    global db_conn
    db_conn = sqlite3.connect(db_filename)
    global cursor
    cursor = db_conn.cursor()
    cursor.execute('''CREATE TABLE SRN
             (REAL latitude, REAL longitude, INT severity, DATETIME timestamp);''')
    cursor.execute('''USE database_name;''')


# function to add stranger to database
def report_stranger(lat, long, severity=1):
    global cursor

    cursor.execute("INSERT INTO SRN (?,?,?,?);", lat, long, severity, datetime.datetime.now().strftime())
    return


def send_closest_srn(lat_user, long_user):
    global cursor
    table = cursor.fetchall()
    return_array = []
    for row in table:
        if haversine((row[0],row[1]), (lat_user, long_user), unit="mi") < 5:
            curr_time = datetime.datetime.now()
            timestamp = row[3]
            datetime_obj = dt_parser.parse(timestamp)
            # find the difference between current time and arrival time
            delta_time = datetime_obj - curr_time
            # find the total number of days
            days = delta_time.total_seconds() % 86400
            if days <= 2:
                return_array.append({"lat": row[0], "long": row[1]})

    return return_array

