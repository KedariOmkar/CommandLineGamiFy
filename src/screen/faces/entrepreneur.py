import sys
import os
import traceback

# Assuming entrepreneur.py is in the faces directory
sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")

from src.common import common_functions
from src.common.common_constants import var
from src.database.mysql_connection import sql



# --------------------------------------------------------------------------------------------------------------------

def character_level():

    softs = percentage_calculate('softs','skill_en','king')
    busi = percentage_calculate('busi','skill_en','king')



    character_skill_mastery = int(softs+busi)

    return character_skill_mastery


def percentage_calculate(field,table_name, level):
    fetch_skills = f"select COUNT(id) from {table_name} where field = '{field}'"
    sql.server.execute(fetch_skills)
    for x in sql.server:
        total_count = int(x[0])

    fetch_king_skills = f"select count(id) from {table_name} where field = '{field}' and level ='{level}'"
    sql.server.execute(fetch_king_skills)
    for x in sql.server:
        total_king_skills = int(x[0])

    if total_king_skills != 0:
        field_percentage = int((total_king_skills / total_count) * 100)
    else:
        field_percentage = 0

    return field_percentage


while True:
    try:
        os.system('cls')

        print("\n")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t# ENTREPRENEUR ::",character_level() , "Weapons")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t1. SOFTS - ",percentage_calculate('softs','skill_en','king'),"%")
        print("\t2. BUSIN - ",percentage_calculate('busi','skill_en','king'),"%")
        print("---------------------------------------------------------------------------------------------------------------")

        try:
            select = int(input("# Field: "))
            while select not in [1, 2, 0]:
                select = int(input("# Field: "))
                print("--")
        except:
            print("Error: Enter Right Fields..")


        if select == 1:
            # softs
            common_functions.skill_info('skill_en', 'softs')
            common_functions.accept_skill()
            if common_functions.select_option == 1:
                common_functions.update_db('skill_en', 'mission_learn', 'time_learn', 'softs', 'report_time_learn', 'report_mission_learn')
            if common_functions.select_option == 2:
                common_functions.update_db('skill_en', 'mission_recall', 'time_recall', 'softs', 'report_time_recall', 'report_mission_recall')
            if common_functions.select_option == 3:
                common_functions.update_db('skill_en', 'mission_test', 'time_test', 'softs', 'report_time_test', 'report_mission_test')
            common_functions.money_earned()
            common_functions.refresh_update()

            if common_functions.select_option == 0:
                os.system(var.entrepeneur_screen)

        # Selects Business Skills
        if select == 2:
            # busi
            common_functions.skill_info('skill_en', 'busi')
            common_functions.accept_skill()
            if common_functions.select_option == 1:
                common_functions.update_db('skill_en', 'mission_learn', 'time_learn', 'busi', 'report_time_learn',
                                           'report_mission_learn')
            if common_functions.select_option == 2:
                common_functions.update_db('skill_en', 'mission_recall', 'time_recall', 'busi', 'report_time_recall',
                                           'report_mission_recall')
            if common_functions.select_option == 3:
                common_functions.update_db('skill_en', 'mission_test', 'time_test', 'busi', 'report_time_test',
                                           'report_mission_test')
            common_functions.money_earned()
            common_functions.refresh_update()

            if common_functions.select_option == 0:
                os.system(var.entrepeneur_screen)

        if select == 0:
            os.system(var.home_screen)

    except Exception as e:
        traceback.print_exc()
        print("\t\t! Exception:", e)
