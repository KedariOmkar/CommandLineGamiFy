import sys
import os
import traceback

sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")

from src.common import common_functions
from src.common.common_constants import var
from src.database.mysql_connection import sql


# --------------------------------------------------------------------------------------------------------------------


def character_level():

    lang = percentage_calculate("lang", "skill_tg", "king")
    dsa = percentage_calculate("dsa", "skill_tg", "king")
    sub = percentage_calculate("sub", "skill_tg", "king")
    tech = percentage_calculate("tech", "skill_tg", "king")
    tools = percentage_calculate("tools", "skill_tg", "king")
    build = percentage_calculate("build", "skill_tg", "king")

    character_skill_mastery = int(lang + dsa + sub + tech + tools + build)

    return character_skill_mastery


def percentage_calculate(field, table_name, level):
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
        os.system("cls")

        print("\n")
        print(
            "---------------------------------------------------------------------------------------------------------------"
        )
        print("\t# TECHGENIUS ::", character_level())
        print(
            "---------------------------------------------------------------------------------------------------------------"
        )
        print("\t1. LANG - ", percentage_calculate("lang", "skill_tg", "king"), "%")
        print("\t2. DSA - ", percentage_calculate("dsa", "skill_tg", "king"), "%")
        print("\t3. SUB - ", percentage_calculate("sub", "skill_tg", "king"), "%")
        print("\t4. TECH - ", percentage_calculate("tech", "skill_tg", "king"), "%")
        print("\t5. TOOLS - ", percentage_calculate("tools", "skill_tg", "king"), "%")
        print("\t6. BUILD - ", percentage_calculate("build", "skill_tg", "king"), "%")

        print(
            "---------------------------------------------------------------------------------------------------------------"
        )

        try:
            select = int(input("# Field: "))
            while select not in [1, 2, 3, 4, 5, 6, 0]:
                select = int(input("# Field: "))
                print("--")
        except:
            print("Error: Enter Right Fields..")

        if select == 1:
            # lang
            common_functions.skill_info("skill_tg", "lang")
            common_functions.accept_skill()
            if common_functions.select_option == 1:
                common_functions.update_db(
                    "skill_tg",
                    "mission_learn",
                    "time_learn",
                    "lang",
                    "report_time_learn",
                    "report_mission_learn",
                )
            if common_functions.select_option == 2:
                common_functions.update_db(
                    "skill_tg",
                    "mission_recall",
                    "time_recall",
                    "lang",
                    "report_time_recall",
                    "report_mission_recall",
                )
            if common_functions.select_option == 3:
                common_functions.update_db(
                    "skill_tg",
                    "mission_test",
                    "time_test",
                    "lang",
                    "report_time_test",
                    "report_mission_test",
                )
            common_functions.money_earned()
            common_functions.refresh_update()

            if common_functions.select_option == 0:
                os.system(var.techgenius_screen)

        # Selects Business Skills
        if select == 2:
            # busi
            common_functions.skill_info("skill_tg", "dsa")
            common_functions.accept_skill()
            if common_functions.select_option == 1:
                common_functions.update_db(
                    "skill_tg",
                    "mission_learn",
                    "time_learn",
                    "dsa",
                    "report_time_learn",
                    "report_mission_learn",
                )
            if common_functions.select_option == 2:
                common_functions.update_db(
                    "skill_tg",
                    "mission_recall",
                    "time_recall",
                    "dsa",
                    "report_time_recall",
                    "report_mission_recall",
                )
            if common_functions.select_option == 3:
                common_functions.update_db(
                    "skill_tg",
                    "mission_test",
                    "time_test",
                    "dsa",
                    "report_time_test",
                    "report_mission_test",
                )
            common_functions.money_earned()
            common_functions.refresh_update()

            if common_functions.select_option == 0:
                os.system(var.techgenius_screen)

        if select == 3:
            # busi
            common_functions.skill_info("skill_tg", "sub")
            common_functions.accept_skill()
            if common_functions.select_option == 1:
                common_functions.update_db(
                    "skill_tg",
                    "mission_learn",
                    "time_learn",
                    "sub",
                    "report_time_learn",
                    "report_mission_learn",
                )
            if common_functions.select_option == 2:
                common_functions.update_db(
                    "skill_tg",
                    "mission_recall",
                    "time_recall",
                    "sub",
                    "report_time_recall",
                    "report_mission_recall",
                )
            if common_functions.select_option == 3:
                common_functions.update_db(
                    "skill_tg",
                    "mission_test",
                    "time_test",
                    "sub",
                    "report_time_test",
                    "report_mission_test",
                )
            common_functions.money_earned()
            common_functions.refresh_update()

            if common_functions.select_option == 0:
                os.system(var.techgenius_screen)

        if select == 4:
            # busi
            common_functions.skill_info("skill_tg", "tech")
            common_functions.accept_skill()
            if common_functions.select_option == 1:
                common_functions.update_db(
                    "skill_tg",
                    "mission_learn",
                    "time_learn",
                    "tech",
                    "report_time_learn",
                    "report_mission_learn",
                )
            if common_functions.select_option == 2:
                common_functions.update_db(
                    "skill_tg",
                    "mission_recall",
                    "time_recall",
                    "tech",
                    "report_time_recall",
                    "report_mission_recall",
                )
            if common_functions.select_option == 3:
                common_functions.update_db(
                    "skill_tg",
                    "mission_test",
                    "time_test",
                    "tech",
                    "report_time_test",
                    "report_mission_test",
                )
            common_functions.money_earned()
            common_functions.refresh_update()

            if common_functions.select_option == 0:
                os.system(var.techgenius_screen)

        if select == 5:
            # busi
            common_functions.skill_info("skill_tg", "tools")
            common_functions.accept_skill()
            if common_functions.select_option == 1:
                common_functions.update_db(
                    "skill_tg",
                    "mission_learn",
                    "time_learn",
                    "tools",
                    "report_time_learn",
                    "report_mission_learn",
                )
            if common_functions.select_option == 2:
                common_functions.update_db(
                    "skill_tg",
                    "mission_recall",
                    "time_recall",
                    "tools",
                    "report_time_recall",
                    "report_mission_recall",
                )
            if common_functions.select_option == 3:
                common_functions.update_db(
                    "skill_tg",
                    "mission_test",
                    "time_test",
                    "tools",
                    "report_time_test",
                    "report_mission_test",
                )
            common_functions.money_earned()
            common_functions.refresh_update()

            if common_functions.select_option == 0:
                os.system(var.techgenius_screen)

        if select == 6:
            # busi
            common_functions.skill_info("skill_tg", "build")
            common_functions.accept_skill()
            if common_functions.select_option == 1:
                common_functions.update_db(
                    "skill_tg",
                    "mission_learn",
                    "time_learn",
                    "build",
                    "report_time_learn",
                    "report_mission_learn",
                )
            if common_functions.select_option == 2:
                common_functions.update_db(
                    "skill_tg",
                    "mission_recall",
                    "time_recall",
                    "build",
                    "report_time_recall",
                    "report_mission_recall",
                )
            if common_functions.select_option == 3:
                common_functions.update_db(
                    "skill_tg",
                    "mission_test",
                    "time_test",
                    "build",
                    "report_time_test",
                    "report_mission_test",
                )
            common_functions.money_earned()
            common_functions.refresh_update()

            if common_functions.select_option == 0:
                os.system(var.techgenius_screen)

        if select == 0:
            os.system(var.home_screen)

    except Exception as e:
        traceback.print_exc()
        print("\t\t! Exception:", e)
