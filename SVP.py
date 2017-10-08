# sqlite3 commands taken from https://docs.python.org/2/library/sqlite3.html

import sqlite3

class State_VS_Productivity():
    
    def __init__(self):
        self.conn = sqlite3.connect('stateVSproductivity_DATA.db')
        self.c = self.conn.cursor()

    def __repr__(self):
        # incomplete repr
        s = ''
        return s

    def get_new_data(self):

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

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS state_prod_RAW (day text, date text, wake_up_time real, 
            bedtime_that_night real, total_sleep_hours_that_night real,
            sleep_quality_that_night real, feeling real, exercise real,
            productivity real)''')

    def modify_db(self):
        new_dataset = self.get_new_data()
        self.c.execute('INSERT INTO state_prod_RAW VALUES (?,?,?,?,?,?,?,?,?)', new_dataset)


    def print_db(self):
        print()
        print("Your State-VS-Productivity database: ")
        
        self.c.execute ('SELECT * FROM state_prod_RAW ') 
        for row in self.c.fetchall():
            print(row)

        print()

    def close_db(self):
        # commit changes and close database
        self.conn.commit()
        self.conn.close()

    def add_new_dataset(self):
        self.modify_db()
        self.print_db()
