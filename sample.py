import pymysql.cursors
import pandas as pd

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='tatsuru',
                             password='Tatsuru@320',
                             database='wataru_private',
                             cursorclass=pymysql.cursors.DictCursor)

tables = ["_accelerometer_ALL","_barometer_ALL","_battery_ALL","_battery_charges_ALL","_gyroscope_ALL","_location_ALL","_screen_ALL","accelerometer","aware_device","barometer","battery","battery_charges","battery_discharges","gyroscope","ios_aware_log","ios_status_monitor","label","locations","mqtt_history","screen"]

for item in tables:
    sql = """SELECT * FROM {};""".format(item)
    df = pd.read_sql(sql, connection)
    df.to_csv('./data/{}.csv'.format(item))