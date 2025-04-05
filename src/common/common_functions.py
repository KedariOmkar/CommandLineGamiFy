import sys
import os

sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")

import datetime
import subprocess
from src.common.common_constants import *
from src.common.common_imports import *
from src.database.mysql_connection import sql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ---------------------------------------------------------------------------------------------------------------------

"""
    FUNCTIONS : Skills related screen
    
"""

""" 

    Function which fetches the skills 
 
"""
# def show_skill_info(skill_table_name, skill_field_name, skill_level_name):
#     """
#         Display information about skills based on the provided criteria.
#
#         Args:
#             skill_table_name (str): The name of the table in the database.
#             skill_field_name (str): The field or category of skills to filter.
#             skill_level_name (str): The skill_level_name of skills to filter.
#
#         Raises:
#             Exception: An exception is raised if there is an error in executing the SQL query.
#
#         Returns:
#             None
#
#         Prints:
#             Skill information in a formatted way, including skill ID, name, total time,
#             and total missions for the specified skill criteria.
#         """
#
#     try:
#         skill_fetch = f"select * from {skill_table_name} where field = '{skill_field_name}' and skill_level_name = '{skill_level_name}'"
#         sql.server.execute(skill_fetch)
#         for x in sql.server:
#             id = x[0]
#             name = x[1].upper()
#             field = x[2]
#             skill_level_name = x[3]
#             time_learn = x[4]
#             time_recall = x[5]
#             time_test = x[6]
#             mission_learn = x[7]
#             mission_recall = x[8]
#             mission_test = x[9]
#
#             total_time = int(time_learn + time_recall + time_test / 60)
#             total_mission = int(mission_learn + mission_recall + mission_test)
#
#             print("\t- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
#             print(f"\t\t# {id}  #  {name}   # {total_time} hr   #  {total_mission} ms")
#             print("\t- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
#
#     except Exception as e:
#         print("\t\t! Exception - skill_info():", e)
#         traceback.print_exc()

def fetch_and_display_skills(skill_table_name, skill_field_name, skill_level_name):
    """
    Fetch skills from the database based on specified criteria and display the information.

    Args:
        skill_table_name (str): The name of the table in the database.
        skill_field_name (str): The field or category of skills to filter.
        skill_level_name (str): The level of skills to filter.

    Raises:
        Exception: An exception is raised if there is an error in executing the SQL query.

    Returns:
        None
    """
    try:
        # SQL query to fetch skill information based on provided criteria
        skill_query = f"SELECT * FROM {skill_table_name} WHERE field = '{skill_field_name}' AND level = '{skill_level_name}'"
        sql.server.execute(skill_query)

        # Display skill information in a formatted way
        for skill_data in sql.server:
            id, name, field, skill_level_name, time_learn, time_recall, time_test, mission_learn, mission_recall, mission_test = skill_data

            # Calculate total time and total missions
            total_time = int((time_learn + time_recall + time_test) / 60)
            total_mission = int(mission_learn + mission_recall + mission_test)

            # Display formatted skill information
            print("\t- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            print(f"\t\t# {id}  #  {name.upper()}   # {total_time} hr   #  {total_mission} ms")
            print("\t- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        # Log a success message
    except Exception as e:
        print("\t\t! An error occurred while fetching and displaying skills. Please try again later.")
        traceback.print_exc()


""" Function which converts the number to inr """
def number_to_inr(amount):
    return "₹{:,.2f}".format(amount)

def print_skill_level_header(skill_level):
    """
    Print the header for a given skill level.

    Parameters:
    - skill_level (str): The skill level for which the header is printed.

    Returns:
    None
    """
    print(f"\n :: {skill_level.capitalize()} ::")

def skill_info(skill_table_name, skill_field_name):
    """
    Fetch and display skills for various skill levels.

    Parameters:
    - skill_table_name (str): The name of the table containing skills.
    - skill_field_name (str): The name of the field containing skill data.

    Returns:
    None
    """
    try:

        skill_levels = ['average','intermediate', 'pro', 'king']

        for level in skill_levels:
            print_skill_level_header(level)
            fetch_and_display_skills(skill_table_name, skill_field_name, level)


    except Exception as e:
        print("\t\t! Exception - skill_info(): %s", e)


def accept_skill():
    """
    Accept user input for skill-related actions.

    The function prompts the user for a Skill Id and an action (Learn, Recall, Test).
    It sets global variables `take_id` and `select_option` accordingly.

    Returns:
    None
    """
    try:
        global take_id
        print("--")
        take_id = int(input("\t# Skill Id: "))
        print("--")

        if take_id == 0:
            os.system(var.home_screen)
        else:
            print("\t\t! Work -  1.[ Learn ]   2.[ Recall ]   3.[ Test ]")
            print("--")
            global select_option
            select_option = int(input("\t# Select: "))

            if select_option == 0:
                os.system(var.home_screen)

    except ValueError as ve:
        print("\t\t! Error - Please enter a valid numeric Skill Id.")
    except Exception as e:
        print("\t\t! Exception - accept_skill():", e)

def update_db(skill_table, skill_mission, skill_time, skill_field_name, report_time_table, report_mission_table):
    """
    Update the database with mission and time details.

    Parameters:
    - skill_table (str): The name of the skill table.
    - skill_mission (str): The field representing mission count in the skill table.
    - skill_time (str): The field representing time count in the skill table.
    - skill_field_name (str): The field name used in the report tables.
    - report_time_table (str): The name of the table storing time-related reports.
    - report_mission_table (str): The name of the table storing mission-related reports.

    Returns:
    None
    """
    try:
        start_time = time.time()
        global worked
        print("--")

        print("---------------------------------------------- TIME STARTED ------------------------------------------------------")
        accept = int(input("\t\t# Start:  "))

        if accept == 1:
            print("------------------------------------------------- MISSIONS ---------------------------------------------------- ")

            # Initialize mission count
            global count
            count = 0

            while True:
                done = int(input(f"\t\t# Mission Done - {count}: "))

                if done == 1:
                    count += 1
                    # Update mission count in the skill_table
                    sql.server.execute(f"UPDATE {skill_table} SET {skill_mission} = {skill_mission} + 1 WHERE id = {take_id}")

                    # Update mission count in report_mission table
                    sql.server.execute(f"UPDATE {report_mission_table} SET {skill_field_name} = {skill_field_name} + 1 WHERE cur_date = CURDATE()")

                    # Update earned money in game_bank
                    sql.server.execute(f"UPDATE game_bank SET earned = earned + {var.reward_money} WHERE account_id = 'ONK'")

                    # Update mission count in report_money table
                    sql.server.execute(f"UPDATE report_money SET mission = mission + {var.reward_money} WHERE cur_date = CURDATE()")

                else:
                    break

            print("----------------------------------------------TIME ENDED---------------------------------------------------- ")

            end_time = time.time()
            worked = int((end_time - start_time) / 60)

            # Update skill time in skill_table
            sql.server.execute(f"UPDATE {skill_table} SET {skill_time} = {skill_time} + {worked} WHERE id = {take_id}")

            # Update time count in report_time table
            sql.server.execute(f"UPDATE {report_time_table} SET {skill_field_name} = {skill_field_name} + {worked} WHERE cur_date = CURDATE()")

            # Update earned money in game_bank
            sql.server.execute(f"UPDATE game_bank SET earned = earned + {worked * var.reward_money} WHERE account_id = 'ONK'")

            # Update time count in report_money table
            sql.server.execute(f"UPDATE report_money SET times = times + {var.reward_money} WHERE cur_date = CURDATE()")

        elif accept == 0:
            os.system(var.home_screen)


    except ValueError as ve:
        print("\t\t! Error - Invalid input:", ve)
    except Exception as e:
        print("\t\t! Exception - update_db():", e)


def money_earned():
    """
    Calculate and display the earned money, considering time and mission rewards.

    Returns:
    None
    """
    try:
        time_money = int(worked * var.reward_money)/10000000
        mission_money = int(count * var.reward_money)/10000000
        total_money = int(time_money + mission_money)/10000000

        print("")
        print("\t # Time:", number_to_inr(time_money))
        print("\t # Mission:", number_to_inr(mission_money))
        print("\t $ Earned:", number_to_inr(total_money),"Cr")
        print("\t-----------------------------")
        print("\t\t ### CONTRACT ###")
        print("\t-----------------------------")

        time.sleep(5)

    except Exception as e:
        print("\t\t! Exception - money_earned():", e)

""" Function which updates the refresh """
def get_total_count(report_name, total_name):
    """
    Get the total count for a specific report and update the corresponding total field.

    Parameters:
    - report_name (str): The name of the report table.
    - total_name (str): The name of the field representing the total count.

    Returns:
    None
    """
    fetch_sum = f"SELECT SUM(atma + brain + body + lang + dsa + sub + tech + tools + build + softs + busi) FROM {report_name} WHERE cur_date = CURDATE()"
    sql.server.execute(fetch_sum)
    for x in sql.server:
        total_sum_fetched = int(x[0])

    update_sum = f"UPDATE {report_name} SET {total_name} = {total_sum_fetched} WHERE cur_date = CURDATE()"
    sql.server.execute(update_sum)
    sql.engine.commit()

def get_total_agents_count():
    """
    Get the total count for game_matrix_agents and update the total_agents_killed field.

    Returns:
    None
    """
    fetch_sum = "SELECT SUM(youtubers + celebs + actors + speakers + pornstars + singers + girlfriends + influencers + relatives + comedians) FROM game_matrix_agents WHERE cur_date = CURDATE()"
    sql.server.execute(fetch_sum)
    for x in sql.server:
        total_sum_agents = x[0]

    update_total_sum = f"UPDATE game_matrix_agents SET total_agents_killed = {total_sum_agents} WHERE cur_date = CURDATE()"
    sql.server.execute(update_total_sum)

def get_total_money_count():
    """
    Get the total money count for report_money and update the total_money field.

    Returns:
    None
    """
    fetch_sum = "SELECT SUM(times + mission + lifestyle + matrix + tasks) FROM report_money WHERE cur_date = CURDATE()"
    sql.server.execute(fetch_sum)
    for x in sql.server:
        total_sum = x[0]

    update_total_sum = f"UPDATE report_money SET total_money = {total_sum} WHERE cur_date = CURDATE()"
    sql.server.execute(update_total_sum)
    sql.engine.commit()

def refresh_update():
    """
    Refresh and update various counts in the database.

    This function updates total time, total mission, total agents killed, total money,
    and performs additional updates on the database.

    Returns:
    None
    """
    try:
        # Calling all the missions

        for report_mission in ['report_mission_learn', 'report_mission_recall', 'report_mission_test']:
            get_total_count(report_mission,'total_mission')

        for report_time in ['report_time_learn', 'report_time_recall', 'report_time_test']:
            get_total_count(report_time, 'total_time')

        # Update enemies
        get_total_agents_count()

        # Update Money
        get_total_money_count()


    except Exception as e:
        traceback.print_exc()
        print("\t\t! Exception - refresh_update():", e)

def get_total_value_today(total_value, skill_table_name):
    """
    Get the total value for a specific field from a given skill table for the current date.

    Parameters:
    - total_value (str): The name of the field to retrieve the total value.
    - skill_table_name (str): The name of the skill table.

    Returns:
    int: The total value for the specified field and table.
    """
    try:
        fetch_total = f"SELECT SUM({total_value}) FROM {skill_table_name} WHERE cur_date = CURDATE()"
        sql.server.execute(fetch_total)
        result = sql.server.fetchone()  # Fetch one result

        # Check if the result is not None before accessing its value
        if result is not None:
            total_sum = result[0]
            return total_sum
        else:
            return 0  # Return a default value if result is None

    except Exception as e:
        raise ValueError(f"Error getting total value for {total_value} in {skill_table_name}: {e}")

def update_money(field, count):
    """
    Update the specified field in the report_money table for the current date.

    Parameters:
    - field (str): The field to update.
    - count (int): The value to update.

    Returns:
    None
    """
    try:
        update_query = f"UPDATE report_money SET {field} = {count} WHERE cur_date = CURDATE()"
        sql.server.execute(update_query)
        sql.engine.commit()
    except Exception as e:
        traceback.print_exc()
        raise ValueError(f"Error updating {field} in report_money: {e}")

def today_stats():
    """
    Calculate and update the money earned today based on various skill tables.

    Returns:
    None
    """
    try:
        # Time
        learn_time = get_total_value_today('total_time', 'report_time_learn')
        recall_time = get_total_value_today('total_time', 'report_time_recall')
        test_time = get_total_value_today('total_time', 'report_time_test')
        total_time = int((learn_time + recall_time + test_time) * var.reward_money)

        # Missions
        learn_mission = get_total_value_today('total_mission', 'report_mission_learn')
        recall_mission = get_total_value_today('total_mission', 'report_mission_recall')
        test_mission = get_total_value_today('total_mission', 'report_mission_test')
        total_mission = int((learn_mission + recall_mission + test_mission) * var.reward_money)

        # Other Counts
        routine_count = int(get_total_value_today('total_routine', 'character_routine') * var.reward_money)
        matrix_count = int(get_total_value_today('total_agents_killed', 'game_matrix_agents') * var.reward_money)

        # Update Money
        update_money('mission', total_mission)
        update_money('times', total_time)
        update_money('lifestyle', routine_count)
        update_money('matrix', matrix_count)

        # Update total money
        fetch_money_count = "SELECT SUM(times + mission + lifestyle + matrix + tasks) FROM report_money WHERE cur_date = CURDATE()"
        sql.server.execute(fetch_money_count)
        for x in sql.server:
            total_count = x[0]

        update_total_money = f"UPDATE report_money SET total_money = {total_count} WHERE cur_date = CURDATE()"
        sql.server.execute(update_total_money)
        sql.engine.commit()

    except Exception as e:
        traceback.print_exc()
        raise ValueError(f"Error calculating and updating today's stats: {e}")

def refresh_database():
    """
    Refresh and update various counts in the database.

    This function updates total time, total mission, total agents killed, total money,
    and performs additional updates on the database.

    Returns:
    None
    """
    try:
        today_stats()
    except Exception as e:
        traceback.print_exc()
        print("\t\t! Exception - refresh_database():", e)

""" Function which converts the number to inr amount """

def numer_to_inr(amount):
    return "₹{:,.2f}".format(amount)

def open_browser(urls):
    # Path to the Brave browser executable
    brave_path = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
    # C:\Program Files\Internet Explorer

    # # Set up options for Brave in incognito mode
    # options = Options()
    # options.binary_location = brave_path
    # options.add_argument("--incognito")
    #
    # # Initialize the WebDriver with the Brave options
    driver = webdriver.Chrome()

    # Open tabs in incognito window
    for images in urls:
        driver.execute_script(f"window.open('{images}', '_blank');")

    # Ask the user if they want to quit
    quit_choice = input("\t! Quit: (1/0) : ")

    if quit_choice == "1":
        # Close the WebDriver
        print("\t! Closing")
        driver.quit()
    else:
        print("Browser remains open.")


""" Function which terminates the application """
def terminate_application(window_title):
    try:
        for process in psutil.process_iter(['pid', 'name', 'cmdline']):
            if "msedge.exe" in process.info['name'].lower() and window_title in " ".join(process.info['cmdline']).lower():
                try:
                    p = psutil.Process(process.info['pid'])
                    p.terminate()
                    p.wait(timeout=5)  # Optional: wait for the process to terminate (timeout in seconds)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as ex:
        print("Error in Terminate Application")
        pass


""" Function which gives the current date """
def get_date():
    try:
        query = "select CURDATE()"
        sql.server.execute(query)
        for x in sql.server:
            cur_date = x[0]
        return cur_date

    except Exception as e:
        print("\t\t! Exception - get_date():", e)

""" Function which converts the number to words """
def number_to_words_inr(number):
    words = humanize.intword(number, format='%.2f')
    return words.capitalize()

def update_bank_account():
    try:
        # fetch amount
        fetch_amount = "select earned from game_bank where account_id = 'ONK'"
        sql.server.execute(fetch_amount)
        for x in sql.server:
            earned_money = int(x[0])

        # updated format
        shorted_form = int(earned_money/var.reward_money)

        # update amount
        update_amount = f"update game_bank set earned = {shorted_form} where account_id = 'onk'"
        sql.server.execute(update_amount)
        sql.engine.commit()

    except Exception as e:
        print("\t\t! Exception - update_bank_account():", e)


def fetchFromSetting(game_option):
    try:
        fetch_field = f"select game_value from game_setting where game_option = '{game_option}'"
        sql.server.execute(fetch_field)
        for x in sql.server:
            game_value = x[0]

        return game_value

    except Exception as e:
        print("Error in fetchFromSetting")
        return None


def dayOngoing():
    try:
        start_date_str = fetchFromSetting('startdate')  # Assuming fetchFromSetting returns a string
        start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()

        today = datetime.date.today()
        days_from_start = (today - start_date).days

        return days_from_start

    except Exception as e:
        print("Error in dayOngoing")
        return None