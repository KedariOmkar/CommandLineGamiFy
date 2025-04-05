import sys
import os

sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")


import time
import winsound
import random
from src.common.common_constants import var
from src.common.common_functions import refresh_update, refresh_database
from src.database.mongodb_connection import mongo_cl
from src.database.mysql_connection import sql
from src.common.common_imports import *


# ======================================================================================================================


""" Running this screen in while loop """


while True:
    os.system("cls")

    print(
        "------------------------------------------------------------------------------------------------------------"
    )
    print("\t# SETTING")
    print(
        "------------------------------------------------------------------------------------------------------------"
    )
    print("\t1. ADMIN")
    print("\t2. UPDATE")
    print("\t3. COMPETITION")
    print("\t4. POMODORO")
    print(
        "------------------------------------------------------------------------------------------------------------"
    )

    # Select the option
    selected_option = int(input(":: Option: "))
    print("--")

    # if loop for fetching the selected options
    if selected_option == 0:
        os.system(var.home_screen)  # Exit the main loop

    if selected_option == 1:
        while True:
            os.system("cls")

            print(
                "------------------------------------------------------------------------------------------------------------"
            )
            print("\t# ADMIN")
            print(
                "------------------------------------------------------------------------------------------------------------"
            )
            print("\t1. INSERT DATA")
            print("\t2. RESTART GAME")
            print("\t3. CHANGE VALUE")
            print(
                "------------------------------------------------------------------------------------------------------------"
            )

            # Select the option
            selected_option = int(input(":: Option (0 to go back): "))
            print("--")

            if selected_option == 0:
                break  # Go back to the previous screen

            if selected_option == 1:

                """Common Function to Insert data into skill tables"""

                def insert_data(skill_table, value):
                    skill_name_list = []
                    fetch_skill_names = f"SELECT name FROM {skill_table}"
                    sql.server.execute(fetch_skill_names)
                    for x in sql.server:
                        names = x[0]
                        skill_name_list.append(names)

                    find_max_field_id = (
                        f"SELECT MAX(id) FROM {skill_table} WHERE field = '{value}'"
                    )
                    sql.server.execute(find_max_field_id)
                    max_id = sql.server.fetchone()[0]

                    if max_id is not None:
                        pass
                    else:
                        max_id = starting_count_dict.get(value)

                    print("--")
                    skill_name = input(" :: Skill Name: ")
                    print("--")

                    while skill_name in skill_name_list:
                        print("\t -- Already Present -- ")
                        skill_name = input(" :: Skill Name: ")

                    id = max_id + 1
                    level = "average"
                    learn_time = 0
                    recall_time = 0
                    test_time = 0
                    learn_mission = 0
                    recall_mission = 0
                    test_mission = 0

                    insert_data_query = f"INSERT INTO {skill_table} VALUES ({id}, '{skill_name}', '{value}', '{level}', {learn_time}, '{recall_time}', '{test_time}', '{learn_mission}', '{recall_mission}', '{test_mission}')"
                    sql.server.execute(insert_data_query)
                    sql.engine.commit()
                    print("\t Added Successfully ")

                while True:
                    os.system("cls")

                    print(
                        "------------------------------------------------------------------------------------------------------------"
                    )
                    print("\t# INSERT DATA")
                    print(
                        "------------------------------------------------------------------------------------------------------------"
                    )
                    print(" :: SKILLS ")
                    print("\t\t1. SUPERHUMAN")
                    print("\t\t2. TECH GENIUS")
                    print("\t\t3. ENTREPRENEUR")
                    print(" :: GAME ")
                    print("\t\t4. STORE")
                    print(
                        "------------------------------------------------------------------------------------------------------------"
                    )

                    selected_option = int(input(" :: Option (0 to go back): "))

                    if selected_option == 0:
                        break  # Go back to the previous screen

                    if selected_option == 1:
                        while True:
                            os.system("cls")

                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )
                            print("\t# SUPERHUMAN")
                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )
                            print("\t1. ATMA")
                            print("\t2. BRAIN")
                            print("\t3. BODY")
                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )

                            starting_count_dict = {
                                "atma": 100,
                                "brain": 200,
                                "body": 300,
                            }
                            field_dict = {1: "atma", 2: "brain", 3: "body"}

                            select_field = int(input("Select : "))
                            value = field_dict.get(select_field)

                            if select_field == 0:
                                break  # Go back to the previous screen

                            while True:
                                insert_data("skill_sh", value)

                                print("")
                                another_skill = input(
                                    " ! Again (0 to go back): "
                                ).lower()
                                if another_skill == "0":
                                    break  # Go back to the previous screen

                    if selected_option == 2:
                        while True:
                            os.system("cls")

                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )
                            print("\t# TECH GENIUS")
                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )
                            print("\t1. LANG")
                            print("\t2. DSA")
                            print("\t3. SUB")
                            print("\t4. TECH")
                            print("\t5. TOOLS")
                            print("\t6. BUILD")
                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )

                            starting_count_dict = {
                                "lang": 100,
                                "dsa": 200,
                                "sub": 300,
                                "tech": 400,
                                "tools": 500,
                                "build": 600,
                            }
                            field_dict = {
                                1: "lang",
                                2: "dsa",
                                3: "sub",
                                4: "tech",
                                5: "tools",
                                6: "build",
                            }

                            select_field = int(input("Select Field (0 to go back): "))
                            value = field_dict.get(select_field)

                            if select_field == 0:
                                break  # Go back to the previous screen

                            while True:

                                insert_data("skill_tg", value)

                                print("")
                                another_skill = input(
                                    " ! Again (0 to go back): "
                                ).lower()
                                if another_skill == "0":
                                    break  # Go back to the previous screen

                    if selected_option == 3:
                        while True:
                            os.system("cls")

                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )
                            print("\t# ENTREPRENUER")
                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )
                            print("\t1. SOFTS")
                            print("\t2. BUSI")
                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )

                            starting_count_dict = {"softs": 100, "busi": 200}
                            field_dict = {1: "softs", 2: "busi"}

                            select_field = int(input("Select Field (0 to go back): "))
                            value = field_dict.get(select_field)

                            if select_field == 0:
                                break  # Go back to the previous screen

                            while True:
                                insert_data("skill_en", value)

                                print("")
                                another_skill = input(
                                    " ! Again (0 to go back): "
                                ).lower()
                                if another_skill == "0":
                                    break  # Go back to the previous screen

                    if selected_option == 4:
                        # Store menu options
                        store_options = {
                            1: {
                                "category": "PROFESSIONAL",
                                "fields": ["position", "tags"],
                            },
                            2: {
                                "category": "FINANCIAL",
                                "fields": ["companies", "investments", "liquid"],
                            },
                            3: {
                                "category": "LAVISH",
                                "fields": [
                                    "mansions",
                                    "cars",
                                    "ultra",
                                    "lifestyle",
                                    "hoe",
                                ],
                            },
                            4: {
                                "category": "PERSONAL",
                                "fields": ["self", "parents", "relations"],
                            },
                            5: {
                                "category": "PHILANTHROPIC",
                                "fields": ["Food", "Education", "Climate Change"],
                            },
                        }

                        # Function to insert data into MySQL
                        def insert_into_mysql(
                            ob_name,
                            ob_cat,
                            on_sub_cat,
                            ob_field,
                            ob_price,
                            ob_achieved_date,
                            ob_age,
                            status,
                        ):
                            sql.server.execute(
                                f"insert into objectives (ob_name, ob_cat, ob_sub_cat, ob_field, ob_price, ob_achieved_date, ob_age, status)  values ('{ob_name}','{ob_cat}','{on_sub_cat}','{ob_field}',{ob_price},'{ob_achieved_date}','{ob_age}','{status}')"
                            )
                            sql.engine.commit()

                        # Function to update existing entry in MySQL
                        def update_existing_mysql(
                            ob_name,
                            ob_cat,
                            on_sub_cat,
                            ob_field,
                            ob_price,
                            ob_achieved_date,
                            ob_age,
                            status,
                        ):
                            query = "UPDATE objectives SET ob_name = %s, ob_cat = %s, ob_sub_cat = %s, ob_field = %s, ob_price = %s , ob_achieved_data = %s , ob_age = %s , status = %s WHERE name = %s"
                            values = (
                                ob_name,
                                ob_cat,
                                on_sub_cat,
                                ob_field,
                                ob_price,
                                ob_achieved_date,
                                ob_age,
                                status,
                            )
                            sql.server.execute(query, values)
                            sql.engine.commit()

                        # Function to check if a name already exists in MySQL
                        def name_exists_in_mysql(name):
                            query = "SELECT COUNT(*) FROM objectives WHERE ob_name = %s"
                            sql.server.execute(query, (name,))
                            result = sql.server.fetchone()
                            return result[0] > 0

                        # Function to insert pictures into MongoDB
                        def insert_into_mongodb(name, pic_urls):
                            mongo_cl.update_one(
                                {"ob_name": name},
                                {"$set": {"pics": pic_urls}},
                                upsert=True,
                            )

                        # Function to input data and pics
                        def input_data_and_pics():
                            select = int(input("Select: "))

                            if select == 0:
                                os.system(var.setting_screen)

                            if select not in store_options:
                                print("Invalid option.")
                                return

                            category = store_options[select]["category"]

                            if "fields" in store_options[select]:
                                print(f"\n :: {category}")
                                print(
                                    "------------------------------------------------------------------------------------------------------------"
                                )
                                for i, field in enumerate(
                                    store_options[select]["fields"], start=1
                                ):
                                    print(f"\t{i}. {field.upper()}")
                                print(
                                    "------------------------------------------------------------------------------------------------------------"
                                )

                                field_index = int(input("Select Field: ")) - 1
                                if field_index < 0 or field_index >= len(
                                    store_options[select]["fields"]
                                ):
                                    print("Invalid field selection.")
                                    return

                                field = store_options[select]["fields"][field_index]
                            else:
                                field = store_options[select]["field"]

                            print("\n :: {}".format(field.upper()))
                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )

                            print("\t ::: INFO ::")
                            ob_name = input("\t\t! Object Name: ")

                            # Check if the name already exists in MySQL
                            if name_exists_in_mysql(ob_name):
                                print(f"\nName '{ob_name}' already exists.")
                                update_option = input(
                                    "Do you want to update the existing entry? (yes/no): "
                                ).lower()
                                if update_option == "no":
                                    return

                            ob_cat = input("\t\t! Goal Cat: ")
                            ob_sub_cat = input("\t\t! Sub-Cat: ")
                            ob_field = input("\t\t! Field: ")
                            ob_price = int(input("\t\t! Value (Cr): "))

                            ob_achieved_date = "n"
                            ob_age = 0
                            status = "not owned"

                            # Insert or update data into MySQL
                            if name_exists_in_mysql(ob_name):
                                update_existing_option = input(
                                    "Enter 1 to update the existing entry, 0 to enter a new one: "
                                )
                                if update_existing_option == "1":
                                    update_existing_mysql(
                                        ob_name,
                                        ob_cat,
                                        ob_sub_cat,
                                        ob_field,
                                        ob_price,
                                        ob_achieved_date,
                                        ob_age,
                                        status,
                                    )
                                else:
                                    return
                            else:
                                insert_into_mysql(
                                    ob_name,
                                    ob_cat,
                                    ob_sub_cat,
                                    ob_field,
                                    ob_price,
                                    ob_achieved_date,
                                    ob_age,
                                    status,
                                )

                            print("\t ::: PICS ::")
                            # Input and insert pictures into MongoDB
                            pic_urls = []
                            pic_input = 1
                            while pic_input:
                                pic_url = input(f"\t\t! PIC-{pic_input}: ")
                                pic_urls.append(pic_url)
                                pic_input = int(input("\t\t\t -- Again: "))

                            insert_into_mongodb(ob_name, pic_urls)

                            print("")
                            print("\t :: Inserted Successfully ::")

                        # Main loop
                        while True:
                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )
                            print("\t :: STORE")
                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )
                            print(
                                "\t\t 1.PROFESSIONAL   2.FINANCIAL   3.LAVISH   4.PERSONAL   5.PHILANTHROPIC"
                            )
                            print(
                                "------------------------------------------------------------------------------------------------------------"
                            )

                            try:
                                input_data_and_pics()
                            except ValueError:
                                print("Invalid input. Please enter a number.")

            if selected_option == 2:

                def clear_tables(table_names):
                    for table in table_names:
                        query = f"DELETE FROM {table}"
                        sql.server.execute(query)
                        sql.engine.commit()

                def reset_skill_fields(skill_table_names, skill_table_field):
                    for table in skill_table_names:
                        for field in skill_table_field:
                            query = f"UPDATE {table} SET {field} = 0"
                            sql.server.execute(query)
                            sql.engine.commit()

                def reset_total_tasks():
                    sql.server.execute(
                        "update report_tasks_total set total_tasks_done = 0"
                    )
                    sql.engine.commit()

                    sql.server.execute(
                        "update report_tasks_total set total_tasks_created = 0"
                    )
                    sql.engine.commit()

                def restart():
                    ask_sure = input("\t\t ! ARE YOU SURE TO RESTART (y/n): ").lower()
                    if ask_sure == "y":
                        ask_again = input("\t\t ! PIN - onk : ")
                        if ask_again == "onk":
                            # Fetch table names from the database or provide them as arguments
                            report_tables = [
                                "report_time_learn",
                                "report_time_recall",
                                "report_time_test",
                                "report_mission_learn",
                                "report_mission_recall",
                                "report_mission_test",
                                "character_physiqe_shield",
                                "character_physiqe_sharp",
                                "character_physiqe_silent",
                                "character_routine",
                                "game_matrix_agents",
                                "report_session",
                                "report_money",
                                "game_bank_transaction",
                                "character_habit",
                            ]

                            skill_tables = ["skill_sh", "skill_tg", "skill_en"]
                            skill_fields = [
                                "time_learn",
                                "time_recall",
                                "time_test",
                                "mission_learn",
                                "mission_recall",
                                "mission_test",
                            ]

                            clear_tables(report_tables)
                            reset_skill_fields(skill_tables, skill_fields)
                            reset_total_tasks()
                            print("--")
                            print("\t\t ### GAME RESTARTED ###")
                            print("--")
                            time.sleep(3)
                        else:
                            print("\t\t ABORTED :::")
                    else:
                        os.system(var.setting_screen)

                restart()

            if selected_option == 3:

                def fetch_game_options():
                    fetch_column_names = "SELECT * FROM game_setting"
                    sql.server.execute(fetch_column_names)
                    for x in sql.server:
                        column_option = x[0]
                        column_value = x[1]
                        print(f"\t\t : {column_option} : {column_value}")
                        print("--")

                def update_game_value(game_option, game_value):
                    update_query = f"UPDATE game_setting SET game_value = '{game_value}' where game_option = '{game_option}'"
                    sql.server.execute(update_query)
                    sql.engine.commit()

                while True:
                    os.system("cls")
                    print(
                        "------------------------------------------------------------------------------------------------------------"
                    )
                    print("\t GAME VALUES ")
                    print(
                        "------------------------------------------------------------------------------------------------------------"
                    )
                    fetch_game_options()
                    print(
                        "------------------------------------------------------------------------------------------------------------"
                    )

                    update_option = input("\t\t Update Option (enter 'z' to exit): ")

                    if update_option.lower() == "z":
                        break

                    try:
                        update_value = input(f"\t\t Update Value for {update_option}: ")
                        update_game_value(update_option, update_value)
                        print("\t ## Value Updated ## ")
                        time.sleep(1)
                    except Exception as e:
                        print(f"\t Error: {e}")

                    again = input(" ! Continue updating? (y/n): ")
                    if again.lower() != "y":
                        break

    if selected_option == 2:

        def update_frame():
            while True:
                os.system("cls")
                print(
                    "-------------------------------------------------------------------------------------------------------------------"
                )
                print("\t# QUICK UPDATE ")
                print(
                    "-------------------------------------------------------------------------------------------------------------------"
                )
                print("\t# TABLE :  1.SH    2.TG    3.EN  ")
                print("\t# COUNT :  1.LEARN    2.RECALL   3.TEST  ")
                print(
                    "\t# FIELD :  1.LANG  2.DSA  3.SUB  4.TECH  5.TOOLS  6.BUILD  7.SOFTS  8.BUSI  9.ATMA  10.BRAIN  11.BODY"
                )
                print(
                    "--------------------------------------------------------------------------------------------------------------------"
                )
                print("")
                table = int(input("\t! Table : "))
                count = int(input("\t! Count : "))
                field = int(input("\t! Field: "))
                id = int(input("\t! Id: "))
                time_min = int(input("\t! Time min: "))
                mission_done = int(input("\t! Mission done: "))

                table_dict = {1: "skill_sh", 2: "skill_tg", 3: "skill_en"}

                count_dict = {1: "time_learn", 2: "time_recall", 3: "time_test"}

                field_dict = {
                    1: "lang",
                    2: "dsa",
                    3: "sub",
                    4: "tech",
                    5: "tools",
                    6: "build",
                    7: "softs",
                    8: "busi",
                    9: "atma",
                    10: "brain",
                    11: "body",
                }

                report_dict_time = {
                    1: "report_time_learn",
                    2: "report_time_recall",
                    3: "report_time_recall",
                }

                report_dict_mission = {
                    1: "report_mission_learn",
                    2: "report_mission_recall",
                    3: "report_mission_test",
                }

                # update time in skill table
                update_skill_table_time = f"update {table_dict.get(table)} set {count_dict.get(count)}= {count_dict.get(count)} + {time_min} where id = {id}"
                sql.server.execute(update_skill_table_time)
                sql.engine.commit()

                # update mission in skill table
                update_skill_table_mission = f"update {table_dict.get(table)} set {count_dict.get(count)}= {count_dict.get(count)} + {mission_done} where id = {id}"
                sql.server.execute(update_skill_table_mission)
                sql.engine.commit()

                # update time in report table
                update_time_report = f"update {report_dict_time.get(count)} set {field_dict.get(field)} = {field_dict.get(field)} + {time_min} where cur_date = CURDATE()"
                sql.server.execute(update_time_report)
                sql.engine.commit()

                # update mission in report table
                update_mission_report = f"update {report_dict_mission.get(count)} set {field_dict.get(field)} = {field_dict.get(field)} + {mission_done} where cur_date = CURDATE()"
                sql.server.execute(update_mission_report)
                sql.engine.commit()

                refresh_update()
                refresh_database()

                print("\t ---- Done ----")

                ask = int(input("\t\t\t# Return: "))

                if ask == 0:
                    os.system(var.setting_screen)

        update_frame()

    if selected_option == 3:

        def competition_frame():
            while True:
                os.system("cls")
                print(
                    "-------------------------------------------------------------------------------------------------------------------"
                )
                print("\t# COMPETITION : ")
                print(
                    "-------------------------------------------------------------------------------------------------------------------"
                )
                print("\t# 1. WORK TODAY")
                print(
                    "-------------------------------------------------------------------------------------------------------------------"
                )
                print("")
                take_input = int(input("\t OPTION : "))

                if take_input == 1:
                    # take random values
                    random_time = random.randint(800, 1000)
                    random_mission = random.randint(1000, 2500)
                    random_routine = random.randint(10, 21)
                    random_tasks = random.randint(50, 250)
                    random_kill = random.randint(25, 250)

                    # insert queries
                    def insert_data_into_game_competition(total_value, value):
                        sql.server.execute(
                            f"update game_competition set {total_value} = {value} where cur_date = CURDATE()"
                        )
                        sql.engine.commit()

                    insert_data_into_game_competition("total_time", random_time)
                    insert_data_into_game_competition("total_mission", random_mission)
                    insert_data_into_game_competition("total_routine", random_routine)
                    insert_data_into_game_competition("total_tasks", random_tasks)
                    insert_data_into_game_competition("total_kill", random_kill)

                    # calculate the sum to get the money variable
                    total_money = int(
                        (
                            random_time
                            + random_mission
                            + random_routine
                            + random_tasks
                            + random_kill
                        )
                        * 10000000
                    )

                    insert_data_into_game_competition("total_money", total_money)

                    print("\t\t Inserted Successfully..")
                    time.sleep(2)
                    os.system(var.setting_screen)

                else:
                    os.system(var.setting_screen)

        competition_frame()

    if selected_option == 4:

        def pomodoro():

            def set_timer():
                while True:
                    try:
                        print("---")
                        time_input = input("# Enter Work Time:   ")
                        print("---")
                        time_in_minutes = int(time_input)
                        break
                    except ValueError:
                        print("Please enter a valid number for the time.")

                while True:
                    try:
                        print("---")
                        break_time_input = input("# Enter Break Time:  ")
                        print("---")
                        break_time_in_minutes = int(break_time_input)
                        break
                    except ValueError:
                        print("Please enter a valid number for the break time.")

                return time_in_minutes, break_time_in_minutes

            def start_pomodoro():
                print("\t ### STARTED ###")
                time.sleep(time_in_minutes * 60)
                winsound.PlaySound(
                    "C:\\Users\\kedar\\Downloads\\marvel.wav", winsound.SND_FILENAME
                )
                print("\t ! Work Finished..")
                print("----")
                print("\t\t Break Time....")
                time.sleep(break_time_in_minutes * 60)
                winsound.PlaySound(
                    "C:\\Users\\kedar\\Downloads\\gta.wav", winsound.SND_FILENAME
                )
                print("\t ! Break ended..")
                start_pomodoro()

            if __name__ == "__main__":
                time_in_minutes, break_time_in_minutes = set_timer()
                start_prompt = input(
                    "Ready to start Pomodoro session? (yes/no): "
                ).lower()
                if start_prompt == "yes":
                    start_pomodoro()
                else:
                    print("Pomodoro session aborted.")

        pomodoro()
