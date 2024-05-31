import sys
import os

sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")

from src.common.common_constants import var
from src.database.mongodb_connection import mongo_cl2
from src.database.mysql_connection import sql


# ----------------------------------------------------------------------------------------------------------------------

""" shows the completed tasks """
import os
import time

from src.common.common_functions import refresh_database , open_browser , terminate_application


def tasks_done():
    tick = u'\u2713'
    fetch_done_tasks = f"select * from report_tasks where task_status = 'CHECKED'"
    sql.server.execute(fetch_done_tasks)
    for x in sql.server:
        print("\t\t-----")
        print("\t\t", tick, x[0], " | ", x[1], " | ", x[2], " | ", x[3])

""" shows the to-complete tasks """

def tasks_to_do(task_level):
    fetch_tasks_to_do = f"select * from report_tasks where task_status = 'UNCHECKED' and task_level = '{task_level}'"
    sql.server.execute(fetch_tasks_to_do)
    for x in sql.server:
        print("\t\t-----")
        print("\t\t o ", x[0], " | ", x[1], " | ", x[2] ,"min")

""" Wet Total Count of tasks in list """

def get_count(condition, task_table):
    get_count = f"select count(task_id) from {task_table} where task_status = '{condition}'"
    sql.server.execute(get_count)
    for x in sql.server:
        count = x[0]
        return count

""" calculates the time checked """

def total_time_checked(task_table):
    fetch_time = f"select SUM(task_time) from {task_table} where task_status = 'CHECKED'"
    sql.server.execute(fetch_time)
    for x in sql.server:
        total_time_checked = x[0]

    return total_time_checked

""" calculates the time unchecked """

def total_time_unchecked(task_table):
    fetch_time = f"select SUM(task_time) from {task_table}"
    sql.server.execute(fetch_time)
    for x in sql.server:
        total_time_unchecked = x[0]

    return total_time_unchecked

""" Add tasks to the list """

def add_tasks(task_table):
    while True:

        id_list = []
        fetch_id = f"select task_id from {task_table}"
        sql.server.execute(fetch_id)
        for x in sql.server:
            id_list.append(x[0])

        # Fetch current count
        fetch_current_count = f"select max(task_id) from {task_table}"
        sql.server.execute(fetch_current_count)
        for x in sql.server:
            curr_count = x[0]

        if curr_count == None:
            curr_count = 0
        else:
            curr_count = x[0]

        task_id = curr_count + 1

        os.system('cls')
        print("-")
        print("\t! Task Id:", curr_count + 1)
        print("-")
        task_name = input("\t! Name: ")
        print("-")
        task_time = int(input("\t! Time Needed: "))
        print("-")
        task_level = input("\t! Level [h][m][l]: ")
        check_list = ['h','m','l']
        while task_level not in check_list:
            task_level = input("\t! Level [h][m][l]: ")
        print("--")
        task_reward = input("\t! Reward: ")
        print("--")
        task_status = "UNCHECKED"

        add_tasks_query = f"insert into {task_table} values ( {task_id} , '{task_name}', '{task_time}', '{task_status}','{task_level}')"
        sql.server.execute(add_tasks_query)
        sql.engine.commit()

        # add count
        add_tasks_created = f"update report_tasks_total set total_tasks_created = total_tasks_created + {1}"
        sql.server.execute(add_tasks_created)
        sql.engine.commit()

        # insert documents
        mongo_cl2.insert_one({
            "task_id":f"{task_id}",
            "task_reward":f"{task_reward}"
        })




        print("\n")
        again = int(input("# Again: "))
        if again == 1:
            add_tasks(task_table)
        else:
            os.system(var.task_screen)

""" Function to clear the list """

def get_total_info(total_field):
    get_total_info = f'select {total_field} from report_tasks_total'
    sql.server.execute(get_total_info)
    for x in sql.server:
        total_info = x[0]

    return total_info
def clear(task_table):
    clear_query = f"delete from {task_table}"
    sql.server.execute(clear_query)
    sql.engine.commit()

    # clear collection
    mongo_cl2.delete_many({})
    print("\t ---- List Cleared ----")
    time.sleep(3)

""" Function to Check the task """

def check(task_table):
    # Check if the id is already completed
    checked_id_list = []
    fetch_check_id = f"select task_id from {task_table} where task_status = 'CHECKED'"
    sql.server.execute(fetch_check_id)
    for x in sql.server:
        checked_id_list.append(x[0])

    check_id = int(input("\t> Priority Id: "))

    if check_id in checked_id_list:
        print(" ---- Tasks Already Completed ----")
        time.sleep(2)
        os.system(var.task_screen)

    else:
        print("-")
        completed = input("\t> Completed: ")
        print("-")
        if completed == "1":
            checked_query = f"update {task_table} set task_status = 'CHECKED' where task_id = {check_id}"
            sql.server.execute(checked_query)
            sql.engine.commit()

            add_money = f"update report_money set tasks = tasks + {10000000} where cur_date = CURDATE()"
            sql.server.execute(add_money)
            sql.engine.commit()

            add_total_count = f"update report_tasks_total set total_tasks_done = total_tasks_done + {1}"
            sql.server.execute(add_total_count)
            sql.engine.commit()

            # reward time
            RewardFromTask = mongo_cl2.find_one({"task_id":f"{check_id}"})
            open_browser(RewardFromTask['task_reward'])
            time.sleep(45)
            terminate_application('brave.exe')


            refresh_database()

            print("\t\t ----- Task Completed -----")
            print("\t\t :: Money Earned : $ 1,00,00,000 Cr")

""" Main Screen Function """
while True:
    os.system('cls')
    print("-----------------------------------------------------------------------------------------------------------")
    print("\t # TASKS : ")
    print("-----------------------------------------------------------------------------------------------------------")
    print("\t :: TOTAL :: ")
    print(f"\t\t : Tasks Created - {get_total_info('total_tasks_created')}")
    print(f"\t\t : Tasks Completed - {get_total_info('total_tasks_done')}")
    print("\t :: TODAY ::")
    print(f"\t\t : Tasks Incomplete - {get_count('UNCHECKED','report_tasks')}")
    print(f"\t\t : Tasks Completed - {get_count('CHECKED','report_tasks')}")
    print("-----------------------------------------------------------------------------------------------------------")

    print("\t ::: COMPLETED :::")
    # Level : High
    tasks_done()
    print("-----------------------------------------------------------------------------------------------------------")

    print("\t :: HIGH :: ")
    tasks_to_do('h')
    print("\t :: MEDIUM ::")
    tasks_to_do('m')
    print("\t :: LOW ::")
    tasks_to_do('l')

    print("-----------------------------------------------------------------------------------------------------------")
    print("--")
    print("\t! Options:  1.[ ADD ]   -   2.[ CLEAR ]   -   3.[ CHECK ]  ")
    print("--")
    select = int(input("\t# Select: "))
    print("--")

    if select == 1:
        add_tasks('report_tasks')

    if select == 2:
        clear('report_tasks')

    if select == 3:
        check('report_tasks')

    if select == 0:
        os.system(var.home_screen)
