# sqlite3 commands taken from https://docs.python.org/2/library/sqlite3.html

import sqlite3

# initialize databse
conn = sqlite3.connect('stateVSproductivity_DATA.db')
c = conn.cursor()

def get_new_data():

    day = str(input("Day of the week: "))
    date = str(input("Date: "))
    wake_up_time = input("Wake-up time: ")
    bedtime_that_night = input("Bedtime that night: ")
    total_sleep_hours_that_night = input("Total sleep hours that night: ")
    sleep_quality_that_night = input("Sleep quality that night: ")
    feeling = input("Feeling: ")
    exercise = input("Exercise: ")
    productivity = input("Productivity: ")

    day_dataset = [day, date, wake_up_time, bedtime_that_night,
                   total_sleep_hours_that_night, sleep_quality_that_night,
                   feeling, exercise, productivity]

    return day_dataset

def initialize_db():
    c.execute('''CREATE TABLE IF NOT EXISTS state_prod_RAW (day text, date text, wake_up_time real, 
	bedtime_that_night real, total_sleep_hours_that_night real,
	sleep_quality_that_night real, feeling real, exercise real,
	productivity real)''')

def modify_db():
    new_dataset = get_new_data()
    c.execute('INSERT INTO state_prod_RAW VALUES (?,?,?,?,?,?,?,?,?)', new_dataset)


def print_db():
    c.execute ('SELECT * FROM state_prod_RAW ') 
    for row in c.fetchall():
        print(row)

def close_db():
    # commit changes and close database
    conn.commit()
    conn.close()

def add_new_dataset():
    modify_db()
    print_db()
