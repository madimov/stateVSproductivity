from SVP import *

start = input('\n To open SVP, hit enter, type svp(), and hit enter again: \n\n')

def svp():

    svp = State_VS_Productivity()
    
    svp.create_table()

    data_entry_prompt = "Would you like at a new data set? (y/n): "
    cont = str(input(data_entry_prompt))

    while cont == "y":
        svp.add_new_dataset()
        cont = str(input(data_entry_prompt))

    svp.close_db()

    # print("dont forget to call svp.close_db() when you are done!")
