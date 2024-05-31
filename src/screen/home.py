import sys
import os

sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")


import datetime
import os
import time
from src.common.common_functions import number_to_inr
from src.common.common_constants import var
from src.database.mysql_connection import sql



def run_first():
    """
        Function which is used to run before starting the home.py

        use : it inserts the mysql database rows in the day-to-day tables

    """

    def get_date():
        """
        Fetches the current date (today date) from the database.

        Returns:
            str: The current date fetched from the database.

        Note:
            This function assumes that `sql.server` is a valid database connection object.
        """
        sql.server.execute("SELECT CURDATE()")
        for x in sql.server:
            cur_date = x[0]

        return cur_date

    def insertReportTime(report_table):

        """
            This function inserts the row in the report time
            - learn_time
            - recall_time
            - test_time

            returns : nothing
        """

        insert_query = f"""INSERT INTO {report_table}
                            SELECT '{get_date()}', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                            WHERE NOT EXISTS (
                                SELECT 1
                                FROM {report_table}
                                WHERE cur_date = '{get_date()}'
                            )"""
        sql.server.execute(insert_query)
        sql.engine.commit()

    def insertReportMission(report_table):

        """

            This function inserts the row in the report mission
            - learn_mission
            - recall_mission
            - test_mission

            returns : nothing

        """
        insert_query = f"""INSERT INTO {report_table}
                            SELECT '{get_date()}', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                            WHERE NOT EXISTS (
                                SELECT 1
                                FROM {report_table}
                                WHERE cur_date = '{get_date()}'
    )"""
        sql.server.execute(insert_query)
        sql.engine.commit()

    def insertCharacterRoutine():
        insert_routine = f""" 
            INSERT INTO character_routine
            SELECT '{get_date()}', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            WHERE NOT EXISTS (
                SELECT 1
                FROM character_routine
                WHERE cur_date = '{get_date()}'
);
        """
        sql.server.execute(insert_routine)
        sql.engine.commit()

    def insertCharacterHabits():
        insert_habits = f"""
            INSERT INTO character_habit
            SELECT '{get_date()}', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            WHERE NOT EXISTS (
                SELECT 1
                FROM character_habit
                WHERE cur_date = '{get_date()}'
    )

        """
        sql.server.execute(insert_habits)
        sql.engine.commit()

    def insertCharacterPhysiqeShield():
        insert_workouts = f"""
            INSERT INTO character_physiqe_shield
            SELECT '{get_date()}', 0, 0, 0, 0, 0, 0, 0, 0, 0
            WHERE NOT EXISTS (
                SELECT 1
                FROM character_physiqe_shield
                WHERE cur_date = '{get_date()}'
    )
        """
        sql.server.execute(insert_workouts)
        sql.engine.commit()

    def insertCharacterPhysiqeSharp():
        insert_workouts = f"""
            INSERT INTO character_physiqe_sharp
            SELECT '{get_date()}', 0, 0, 0, 0, 0, 0
            WHERE NOT EXISTS (
                SELECT 1
                FROM character_physiqe_sharp
                WHERE cur_date = '{get_date()}'
    )
        """
        sql.server.execute(insert_workouts)
        sql.engine.commit()

    def insertCharacterPhysiqeSilent():
        insert_workouts = f"""
            INSERT INTO character_physiqe_silent
            SELECT '{get_date()}', 0, 0, 0, 0
            WHERE NOT EXISTS (
                SELECT 1
                FROM character_physiqe_silent
                WHERE cur_date = '{get_date()}'
    )
        """
        sql.server.execute(insert_workouts)
        sql.engine.commit()

    def insertGameMatrixAgents():
        insert_mistakes = f"""
            INSERT INTO game_matrix_agents
            SELECT '{get_date()}', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            WHERE NOT EXISTS (
                SELECT 1
                FROM game_matrix_agents
                WHERE cur_date = '{get_date()}'
            )    
        """
        sql.server.execute(insert_mistakes)
        sql.engine.commit()

    def insertReportMoney():
        insert_money_report = f"""
             INSERT INTO report_money
            SELECT '{get_date()}', 0, 0, 0, 0, 0, 0
            WHERE NOT EXISTS (
                SELECT 1
                FROM report_money
                WHERE cur_date = '{get_date()}'
    )
        """
        sql.server.execute(insert_money_report)
        sql.engine.commit()

    def insertReportCompetition():
        insert_report_competition = f"""
            INSERT INTO game_competition
            SELECT '{get_date()}', 0, 0, 0, 0, 0, 0
            WHERE NOT EXISTS (
                SELECT 1
                FROM game_competition
                WHERE cur_date = '{get_date()}'
    )
        """
        sql.server.execute(insert_report_competition)
        sql.engine.commit()

    # Recall Insert
    insertReportTime('report_time_recall')
    # Test Insert
    insertReportTime('report_time_test')
    # learn Mission
    insertReportMission('report_mission_learn')
    # Recall Mission
    insertReportMission('report_mission_recall')
    # Test Mission
    insertReportMission('report_mission_test')
    # Mistake Insert
    insertGameMatrixAgents()
    # Workout Insert
    insertCharacterPhysiqeShield()
    insertCharacterPhysiqeSharp()
    insertCharacterPhysiqeSilent()
    # Insert Money
    insertReportMoney()
    # Insert Competition
    insertReportCompetition()



    check_list = []
    check_condition = "select cur_date from character_routine where cur_date = CURDATE()"
    sql.server.execute(check_condition)
    for x in sql.server:
        cur_date = x[0]
        check_list.append(cur_date)

    # If else for Checking list
    if len(check_list):
        pass
    else:
        # Routine Insert
        insertCharacterRoutine()
        # Habit insert
        insertCharacterHabits()
        # Learn Insert
        insertReportTime('report_time_learn')
        # Recall Insert
        insertReportTime('report_time_recall')
        # Test Insert
        insertReportTime('report_time_test')
        # learn Mission
        insertReportMission('report_mission_learn')
        # Recall Mission
        insertReportMission('report_mission_recall')
        # Test Mission
        insertReportMission('report_mission_test')
        # Mistake Insert
        insertGameMatrixAgents()
        # Workout Insert
        insertCharacterPhysiqeShield()
        insertCharacterPhysiqeSharp()
        insertCharacterPhysiqeSilent()
        # Insert Money
        insertReportMoney()
        # Insert Competition
        insertReportCompetition()



""" First Function Call """
run_first()



def fetchFromSetting(game_option):
    fetch_field = f"select game_value from game_setting where game_option = '{game_option}'"
    sql.server.execute(fetch_field)
    for x in sql.server:
        game_value = x[0]

    return game_value

""" This functions gives the headings data """
def dayOngoing():
    start_date_str = fetchFromSetting('enddate')  # Assuming fetchFromSetting returns a string
    end_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()

    today = datetime.date.today()
    days_from_start = (end_date - today).days

    return days_from_start
def displayDate():
    today = datetime.date.today()

    return today



""" This function returns the total_value of multiple columsn for complete game """
def getTotalValue(total_value,table_name):
    fetch_total = f"select sum({total_value}) from {table_name}"
    sql.server.execute(fetch_total)
    for x in sql.server:
        total = x[0]
        
    return total

""" This function returns the total_value of multiple columsn for today """
def getTotalValueToday(total_value, table_name):
    fetch_total = f"select sum({total_value}) from {table_name} where cur_date = CURDATE()"
    sql.server.execute(fetch_total)
    for x in sql.server:
        total = x[0]

    return total

def format_inr(amount):
    return "₹{:,.2f}".format(amount)

""" This function returns the total_money earned in the game"""
def getTotalMoney():
    fetch_money = "select sum(total_money) from report_money"
    sql.server.execute(fetch_money)
    for x in sql.server:
        money_earned = (x[0]/10000000)
        formated_money = format_inr(money_earned)

    return formated_money



""" This function returns the total_money earned today """
def getTotalMoneyToday():
    fetch_money = "select sum(total_money) from report_money where cur_date = CURDATE()"
    sql.server.execute(fetch_money)
    for x in sql.server:
        money_earned = int(x[0]/10000000)

    return money_earned


""" This function gives stats for complete game """
def gameStats():
    # Time
    learn_time = getTotalValue('total_time', 'report_time_learn')
    recall_time = getTotalValue('total_time', 'report_time_recall')
    test_time = getTotalValue('total_time', 'report_time_test')

    total_time = int(learn_time + recall_time + test_time)
    target_time = var.target_time
    time_percentage = int((total_time / target_time) * 100)

    # Missions
    learn_mission = getTotalValue('total_mission', 'report_mission_learn')
    recall_mission = getTotalValue('total_mission', 'report_mission_recall')
    test_mission = getTotalValue('total_mission', 'report_mission_test')

    total_mission = int(learn_mission + recall_mission + test_mission)
    target_mission = var.target_mission
    mission_percentage = int((total_mission / target_mission) * 100)

    def total_skills(table_name):
        sql.server.execute(f"select COUNT(id) from {table_name}")
        for x in sql.server:
            total_skill_count = x[0]

        return total_skill_count
    def total_skills_mastered(table_name):
        sql.server.execute(f"select COUNT(id) from {table_name} where level = 'king' ")
        for x in sql.server:
            total_skill_count_mastered = x[0]

        return total_skill_count_mastered


    # Total Skills in tg and en
    tg_skill = total_skills('skill_tg')
    en_skill = total_skills('skill_en')
    # Total Skills
    total_skills_for_gbm = int(tg_skill + en_skill)

    # Skills Acquired in tg and en
    tg_skill_mastered = total_skills_mastered('skill_tg')
    en_skill_mastered = total_skills_mastered('skill_en')
    # Mastered Skill
    total_skills_for_gbm_mastered = int(tg_skill_mastered + en_skill_mastered)


    # Percentage
    weapons_acquired = int((total_skills_for_gbm_mastered / total_skills_for_gbm) * 100)

    # Money
    total_money = getTotalMoney()

    """ printing the stats """

    print("\t :: GAME STATS")
    print(f"\t\t: {var.time_variable} :", total_time, f"{var.time_measure}", " - ", time_percentage, "%")
    print(f"\t\t: {var.mission_variable} :", total_mission, f"{var.mission_measure}", " - ", mission_percentage, "%")
    print(f"\t\t: {var.skill_variable} :",tg_skill_mastered, f"{var.skill_measure}", " - ", weapons_acquired, "%")
    print(f"\t\t: {var.money_variable} :",total_money,"Cr")

""" This function gives stats for todays """
def todayStats():
    # Time
    learn_time = getTotalValueToday('total_time', 'report_time_learn')
    recall_time = getTotalValueToday('total_time', 'report_time_recall')
    test_time = getTotalValueToday('total_time', 'report_time_test')

    total_time = int(learn_time + recall_time + test_time)
    target_time = var.target_time_day
    time_percentage = int((total_time / target_time) * 100)

    # Missions
    learn_mission = getTotalValueToday('total_mission', 'report_mission_learn')
    recall_mission = getTotalValueToday('total_mission', 'report_mission_recall')
    test_mission = getTotalValueToday('total_mission', 'report_mission_test')

    total_mission = int(learn_mission + recall_mission + test_mission)
    target_mission = var.target_mission_day
    mission_percentage = int((total_mission / target_mission) * 100)

    # money
    total_money = getTotalMoneyToday()
    money_percentage = int((total_money / var.target_cash_day) * 100)

    # enemies
    total_enemies = getTotalValueToday('total_agents_killed','game_matrix_agents')
    agent_percentage = int((total_enemies/var.target_agents_kill)*100)

    print("\t :: TODAY STATS")
    print(f"\t\t: {var.time_variable} :", total_time, f"{var.time_measure}", " - ", time_percentage, "%")
    print(f"\t\t: {var.mission_variable} :", total_mission, f"{var.mission_measure}", " - ", mission_percentage, "%")
    print(f"\t\t: {var.money_variable} :",number_to_inr(total_money),f"{var.money_measure}"," - " ,money_percentage,"%")
    print(f"\t\t: {var.agent_variable} :",total_enemies, f"{var.agent_measure}"," - ",agent_percentage,"%" )



""" This function is used to give todays game percentage completion """
def gbmTodayPercentage():
    learn_time = getTotalValueToday('total_time', 'report_time_learn')
    recall_time = getTotalValueToday('total_time', 'report_time_recall')
    test_time = getTotalValueToday('total_time', 'report_time_test')

    total_time = int(learn_time + recall_time + test_time)
    target_time = var.target_time_day
    time_percentage = int((total_time / target_time) * 100)

    # Missions
    learn_mission = getTotalValueToday('total_mission', 'report_mission_learn')
    recall_mission = getTotalValueToday('total_mission', 'report_mission_recall')
    test_mission = getTotalValueToday('total_mission', 'report_mission_test')

    total_mission = int(learn_mission + recall_mission + test_mission)
    target_mission = var.target_mission_day
    mission_percentage = int((total_mission / target_mission) * 100)

    average_game_percentage = int((time_percentage + mission_percentage) / 2)

    return average_game_percentage


""" This function is used to give complete game percentage completion """
def gbmGamePercentage():

    """

        This function shows the percentage of game completed

    """

    # Time
    learn_time = getTotalValue('total_time', 'report_time_learn')
    recall_time = getTotalValue('total_time', 'report_time_recall')
    test_time = getTotalValue('total_time', 'report_time_test')

    total_time = int(learn_time + recall_time + test_time)
    target_time = var.target_time
    time_percentage = int((total_time / target_time) * 100)

    # Missions
    learn_mission = getTotalValue('total_mission', 'report_mission_learn')
    recall_mission = getTotalValue('total_mission', 'report_mission_recall')
    test_mission = getTotalValue('total_mission', 'report_mission_test')

    total_mission = int(learn_mission + recall_mission + test_mission)
    target_mission = var.target_mission
    mission_percentage = int((total_mission / target_mission) * 100)

    average_game_percentage = int((time_percentage+mission_percentage)/2)

    return average_game_percentage




while True:
    os.system('cls')

    print("----")
    print(f" DATE: {displayDate()} -- REMAINING - {dayOngoing()}")
    print("------------------------------------------------------------------------------------------------------------")
    print(f"\t :: {var.core_goal} :: GAME - {gbmGamePercentage()}%  --  TODAY - {gbmTodayPercentage()}%")
    print("------------------------------------------------------------------------------------------------------------")
    gameStats()
    print("")
    todayStats()
    print("------------------------------------------------------------------------------------------------------------")
    print("\t\t1. FACES    2. TASKS    3. STATS    4. CHARACTER    5. MAYA    6. TARGETS    7. SETTINGS    ")
    print("------------------------------------------------------------------------------------------------------------")

    # Select Tab
    select = int(input(" # Select: "))
    print("--")

    if select == 1:
        print("\t\tCharacter :  1.SUPERHUMAN  -  2.TECH GENIUS  -  3.ENTREPRENEUR")

        print("--")
        select_char = int(input(" # Char : "))
        if select_char == 1:
            os.system(var.superhuman_screen)

        if select_char == 2:
            os.system(var.techgenius_screen)

        if select_char == 3:
            os.system(var.entrepeneur_screen)

        if select_char == 0:
            os.system(var.home_screen)

    if select == 2:
        os.system(var.task_screen)

    if select == 3:
        os.system(var.stats_screen)

    if select == 4:
        os.system(var.character_screen)

    if select == 5:
        os.system(var.matrix_screen)

    if select == 6:
        os.system(var.store_screen)

    if select == 7:
        os.system(var.setting_screen)

    if select == 0:
        print(" ---- Exited --- ")
        time.sleep(1)
        os.system("TASKKILL /F /IM python.exe >nul 2>&1")
        print("")


