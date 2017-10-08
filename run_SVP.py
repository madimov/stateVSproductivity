from SVP import *

start = input('\n To open SVP, hit enter, type svp(), and hit enter again: \n\n')

def svp():

    svp = State_VS_Productivity()
    
    svp.create_table()

    svp.add_data()

    svp.close_db()
