import sys
import os


sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")

import time
from datetime import datetime
from src.common.common_constants import var
from src.database.mysql_connection import sql
from src.common.common_imports import *
from src.common.common_functions import open_browser, terminate_application, number_to_inr

# ---------------------------------------------------------------------------------------------------------------------

while True:
    os.system('cls')

    print("------------------------------------------------------------------------------------------------------------")
    print("\t# OPTIONS")
    print("------------------------------------------------------------------------------------------------------------")
    print("  :: CHARACTER")
    print("\t :: LIFESTYLE")
    print("\t\t1. ROUTINE")
    print("\t\t2. HABITS")
    print("\t :: PHYSIQUE")
    print("\t\t3. SHIELD")
    print("\t\t4. SHARP")
    print("\t\t5. SILENT")
    print("  :: BANK")
    print("\t\t6. ACCOUNT")
    print("------------------------------------------------------------------------------------------------------------")

    option = int(input("\t Option: "))

    if option == 0:
        os.system(var.home_screen)

    else:
        if option == 1:
            def routine():

                def check_percentage():
                    fetch_total_routine = "select total_routine from character_routine where cur_date = CURDATE()"
                    sql.server.execute(fetch_total_routine)
                    for x in sql.server:
                        total_count = x[0]

                    target_routine = 25

                    routine_percentage = int((total_count/target_routine)*100)

                    return routine_percentage

                def get_routine_ticked():
                    fetch_ticked = "select total_routine from character_routine where cur_date = CURDATE()"
                    sql.server.execute(fetch_ticked)
                    for x in sql.server:
                        total_ticked = x[0]

                    return total_ticked

                def update_total_routine():
                    fetch_sum = "SELECT SUM(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+x+y+z) FROM character_routine WHERE cur_date = CURDATE()"
                    sql.server.execute(fetch_sum)
                    total_sum = sql.server.fetchone()[0] or 0

                    update_total_sum = f"UPDATE character_routine SET total_routine = {total_sum} WHERE cur_date = CURDATE()"
                    sql.server.execute(update_total_sum)
                    sql.engine.commit()

                while True:
                    os.system('cls')
                    print("------------------------------------------------------------------------------------------------------------")
                    print(f"\t# ROUTINE : {check_percentage()} %   -  TICKED : {get_routine_ticked()}")
                    print("------------------------------------------------------------------------------------------------------------")
                    print(f"\t\t :A. {var.routine_a}")
                    print(f"\t\t :B. {var.routine_b}")
                    print(f"\t\t :C. {var.routine_c}")
                    print(f"\t\t :D. {var.routine_d}")
                    print(f"\t\t :E. {var.routine_e}")
                    print(f"\t\t :F. {var.routine_f}")
                    print(f"\t\t :G. {var.routine_g}")
                    print(f"\t\t :H. {var.routine_h}")
                    print(f"\t\t :I. {var.routine_i}")
                    print(f"\t\t :J. {var.routine_j}")
                    print(f"\t\t :K. {var.routine_k}")
                    print(f"\t\t :L. {var.routine_l}")
                    print(f"\t\t :M. {var.routine_m}")
                    print(f"\t\t :N. {var.routine_n}")
                    print(f"\t\t :O. {var.routine_o}")
                    print(f"\t\t :P. {var.routine_p}")
                    print(f"\t\t :Q. {var.routine_q}")
                    print(f"\t\t :R. {var.routine_r}")
                    print(f"\t\t :S. {var.routine_s}")
                    print(f"\t\t :T. {var.routine_t}")
                    print(f"\t\t :U. {var.routine_u}")
                    print(f"\t\t :V. {var.routine_v}")
                    print(f"\t\t :W. {var.routine_w}")
                    print(f"\t\t :X. {var.routine_x}")
                    print(f"\t\t :Y. {var.routine_y}")
                    print(f"\t\t :Z. {var.routine_z}")
                    print("------------------------------------------------------------------------------------------------")
                    print("--")
                    routine_id = input("\t Enter Id: ")
                    print("--")
                    time.sleep(1)

                    if routine_id == '0':
                        os.system(var.character_screen)

                    if routine_id == 'x':
                        os.system('cls')
                        print("\t :: AMOUNT LOST")


                    else:

                        # see the count
                        see_id = f"select {routine_id} from character_routine where cur_date = CURDATE()"
                        sql.server.execute(see_id)
                        for x in sql.server:
                            result = (x[0])

                        if result == 0:

                            if routine_id == 'a':

                                open_browser('https://cdn.britannica.com/17/155017-050-9AC96FC8/Example-QR-code.jpg')
                                time.sleep(20)
                                open_browser('https://i.pinimg.com/736x/3d/db/e2/3ddbe25363b309c805757ac406168950.jpg')
                                time.sleep(60)
                                terminate_application('brave.exe')

                                def get_up_protocol():
                                    # Get the current time
                                    current_time_hr = datetime.now().strftime('%I')
                                    current_time_min = datetime.now().strftime("%M")
                                    current_time_abbr = datetime.now().strftime("%p")

                                    if int(current_time_hr) == 3 and int(current_time_min) < 25:
                                        # Add money to the account
                                        sql.server.execute(
                                            f'update report_money set lifestyle = lifestyle + {250000000} where cur_date = CURDATE()')
                                        sql.engine.commit()

                                        add_routine_count = f"update character_routine set {routine_id} = {1} where cur_date = CURDATE()"
                                        sql.server.execute(add_routine_count)
                                        sql.engine.commit()

                                        # add the money to bank
                                        add_money_to_bank = f"update game_bank set earned = earned + {250000000}"
                                        sql.server.execute(add_money_to_bank)
                                        sql.engine.commit()

                                        print("\t Credited $25,00,00,000 INR ")
                                        open_browser('https://www.notion.so/Purusharth-d8f445209077449f8f80bf4079670260?pvs=4')
                                        time.sleep(120)
                                        print("\t\t Lets WAR...")

                                get_up_protocol()
                                update_total_routine()

                            else:
                                add_routine_count = f"update character_routine set {routine_id} = {1} where cur_date = CURDATE()"
                                sql.server.execute(add_routine_count)
                                sql.engine.commit()

                                # add the money count
                                add_money_report = f"update report_money set lifestyle = lifestyle + {10000000} where cur_date = CURDATE()"
                                sql.server.execute(add_money_report)
                                sql.engine.commit()

                                # add the money to bank
                                add_money_to_bank = f"update game_bank set earned = earned + {10000000}"
                                sql.server.execute(add_money_to_bank)
                                sql.engine.commit()

                                print("\t\t Routine Ticked.....")

                                update_total_routine()


                        else:
                            time.sleep(2)
                            print("\t Already Ticked...")
                            update_total_routine()

            routine()
            
        if option == 2:
            def habit():

                def check_percentage():
                    fetch_total_habit = "select total_habit from character_habit where cur_date = CURDATE()"
                    sql.server.execute(fetch_total_habit)
                    for x in sql.server:
                        total_count = x[0]

                    target_habit = 25

                    habit_percentage = int((total_count/target_habit)*100)

                    return habit_percentage

                def get_habit_ticked():
                    fetch_ticked = "select total_habit from character_habit where cur_date = CURDATE()"
                    sql.server.execute(fetch_ticked)
                    for x in sql.server:
                        total_ticked = x[0]

                    return total_ticked

                def update_total_habit():
                    fetch_sum = "SELECT SUM(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+x+y+z) FROM character_habit WHERE cur_date = CURDATE()"
                    sql.server.execute(fetch_sum)
                    total_sum = sql.server.fetchone()[0] or 0

                    update_total_sum = f"UPDATE character_habit SET total_habit = {total_sum} WHERE cur_date = CURDATE()"
                    sql.server.execute(update_total_sum)
                    sql.engine.commit()

                while True:
                    os.system('cls')
                    print("------------------------------------------------------------------------------------------------------------")
                    print(f"\t# habit : {check_percentage()} %   -  TICKED : {get_habit_ticked()}")
                    print("------------------------------------------------------------------------------------------------------------")
                    print("\t\t :A. ")
                    print("\t\t :B. ")
                    print("\t\t :C. ")
                    print("\t\t :D. ")
                    print("\t\t :E. ")
                    print("\t\t :F. ")
                    print("\t\t :G. ")
                    print("\t\t :H. ")
                    print("\t\t :I. ")
                    print("\t\t :J. ")
                    print("\t\t :K. ")
                    print("\t\t :L. ")
                    print("\t\t :M. ")
                    print("\t\t :N.")
                    print("\t\t :O. ")
                    print("\t\t :P. ")
                    print("\t\t :Q. ")
                    print("\t\t :R. ")
                    print("\t\t :S. ")
                    print("\t\t :T. ")
                    print("\t\t :U. ")
                    print("\t\t :V. ")
                    print("\t\t :X. ")
                    print("\t\t :Y. ")
                    print("\t\t :Z. ")
                    print("------------------------------------------------------------------------------------------------")
                    print("--")
                    habit_id = input("\t Enter Id: ")
                    print("--")

                    if habit_id == '0':
                        os.system(var.character_screen)
                    else:
                        print("\t\t habit Ticked.....")
                        # see the count
                        see_id = f"select {habit_id} from character_habit where cur_date = CURDATE()"
                        sql.server.execute(see_id)
                        for x in sql.server:
                            result = (x[0])

                        if result == 0:
                            add_habit_count = f"update character_habit set {habit_id} = {habit_id} +  {1} where cur_date = CURDATE()"
                            sql.server.execute(add_habit_count)
                            sql.engine.commit()


                            update_total_habit()


                        else:
                            print("\t Already Ticked...")
                            update_total_habit()

            habit()

        if option == 3:

            def shield():

                def hC(workout):
                    highest_count = f"select MAX({workout}) from character_physiqe_shield"
                    sql.server.execute(highest_count)
                    for x in sql.server:
                        high_count = int(x[0])

                    return high_count

                def tC(workout):
                    today_count = 0  # Default value
                    highest_count = f"select {workout} from character_physiqe_shield where cur_date = CURDATE()"
                    sql.server.execute(highest_count)
                    for x in sql.server:
                        today_count = int(x[0])

                    return today_count

                def get_total_workout():
                    fetch_total_count = "select total_workout from character_physiqe_shield where cur_date = CURDATE()"
                    sql.server.execute(fetch_total_count)
                    for x in sql.server:
                        total_workout = int(x[0])

                    return total_workout

                while True:
                    os.system('cls')
                    start_time = time.time()

                    print("--")

                    print("-------------------------------------------------------------------------------------------------------------------")
                    print("\t # Workout Reps: ", get_total_workout())
                    print("\t # Mission Done :", int(get_total_workout() / 12))
                    print("-------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print(f"\t 1:: CHEST : {tC('chest')}><{hC('chest')}")
                    print("")
                    print(f"\t 2:: BACK : {tC('back')}><{hC('back')}")
                    print("")
                    print(f"\t 3:: SHOULDER : {tC('shoulder')}><{hC('shoulder')}")
                    print("")
                    print(f"\t 4:: ABS : {tC('abs')}><{hC('abs')}")
                    print("")
                    print(f"\t 5:: LEG : {tC('leg')}><{hC('leg')}")
                    print("")
                    print(f"\t 6:: BICEP : {tC('bicep')}><{hC('bicep')}")
                    print("")
                    print(f"\t 7:: TRICEP : {tC('tricep')}><{hC('tricep')}")
                    print("")
                    print(f"\t 8:: FOREARM : {tC('forearm')}><{hC('forearm')}")
                    print("")

                    print("-------------------------------------------------------------------------------------------------------------------")
                    print("")
                    workout_id = int(input("\t\t ::: Workout ID: "))
                    if workout_id == 0:
                        end_time = time.time()
                        diff = int(end_time - start_time)
                        worked = int(diff / 60)

                        # update the workout in skill_sh
                        update_time = f"update skilL_sh set time_recall  = {worked} where id = {302}"
                        sql.server.execute(update_time)
                        sql.engine.commit()

                        # update the workout in skill_sh
                        total_mission = int(get_total_workout()/12)
                        update_mission = f"update skill_sh set mission_recall = {total_mission} where id = {302}"
                        sql.server.execute(update_mission)
                        sql.engine.commit()

                        # update the time in report_table
                        update_time_report = f"update report_time_recall set body = body + {worked} where cur_date = CURDATE()"
                        sql.server.execute(update_time_report)
                        sql.engine.commit()

                        # update the mission in report_table
                        update_mission_report = f"update report_mission_recall set body = body + {total_mission} where cur_date = CURDATE()"
                        sql.server.execute(update_mission_report)
                        sql.engine.commit()


                        # update the money
                        money_time = int(worked*10000000)
                        update_money = f"update report_money set times = times + {money_time} where cur_date = CURDATE()"
                        sql.server.execute(update_money)
                        sql.engine.commit()

                        # update the money mission
                        money_mission = int(total_mission*10000000)
                        update_money_mission = f"update report_money set mission = mission + {money_mission} where cur_date = CURDATE()"
                        sql.server.execute(update_money_mission)
                        sql.engine.commit()

                        # update in bank account
                        total_money_earned = int(money_mission + money_time)
                        money_update_bank = f"update game_bank set earned = earned + {total_money_earned} where account_id = 'onk'"
                        sql.server.execute(money_update_bank)
                        sql.engine.commit()


                        os.system(var.character_screen)
                    else:

                        workout_rep = int(input("\t\t ::: Rep: "))

                        print("")

                        # chest | back | shoulder | abs  | leg  | bicep | tricep | forearm
                        key = {1: 'chest', 2: 'back', 3: 'shoulder', 4: 'abs', 5: 'leg', 6: 'bicep', 7: 'tricep',
                               8: 'forearm'}

                        # Add Count
                        add_count = f"update character_physiqe_shield set {key.get(workout_id)} = {key.get(workout_id)} + {workout_rep} where cur_date = CURDATE()"
                        sql.server.execute(add_count)
                        sql.engine.commit()

                        # update total Count
                        fetch_total_count = "select SUM(chest + back + shoulder + abs  + leg  + bicep + tricep + forearm ) from character_physiqe_shield where cur_date = CURDATE()"
                        sql.server.execute(fetch_total_count)
                        for x in sql.server:
                            total_count = int(x[0])

                        # update the totalCount
                        update_total_count = f"update character_physiqe_shield set total_workout = {total_count} where cur_date = CURDATE()"
                        sql.server.execute(update_total_count)
                        sql.engine.commit()

                        print("\t ------- Workout Done ------- ")

            shield()

        if option == 4:

            def sharp():
                def hC(workout):
                    highest_count = f"select MAX({workout}) from character_physiqe_sharp"
                    sql.server.execute(highest_count)
                    for x in sql.server:
                        high_count = int(x[0])

                    return high_count

                def tC(workout):
                    today_count = 0  # Default value
                    highest_count = f"select {workout} from character_physiqe_sharp where cur_date = CURDATE()"
                    sql.server.execute(highest_count)
                    for x in sql.server:
                        today_count = int(x[0])

                    return today_count

                def get_total_workout():
                    fetch_total_count = "select total_workout from character_physiqe_sharp where cur_date = CURDATE()"
                    sql.server.execute(fetch_total_count)
                    for x in sql.server:
                        total_workout = int(x[0])

                    return total_workout

                while True:
                    os.system('cls')
                    start_time = time.time()
                    print("--")

                    print("-------------------------------------------------------------------------------------------------------------------")
                    print("\t # Workout Reps: ", get_total_workout())
                    print("\t # Mission Done :", int(get_total_workout() / 12))
                    print("-------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print(f"\t 1:: PUNCH : {tC('punch')}><{hC('punch')}")
                    print("")
                    print(f"\t 2:: STRIKE : {tC('strike')}><{hC('strike')}")
                    print("")
                    print(f"\t 3:: KICK : {tC('kick')}><{hC('kick')}")
                    print("")
                    print(f"\t 4:: DEFENSE : {tC('defense')}><{hC('defense')}")
                    print("")

                    print(
                        "-------------------------------------------------------------------------------------------------------------------")
                    print("")
                    workout_id = int(input("\t\t ::: Workout ID: "))
                    if workout_id == 0:
                        end_time = time.time()
                        diff = int(end_time - start_time)
                        worked = int(diff / 60)

                        # update the workout in skill_sh
                        update_time = f"update skilL_sh set time_recall  = {worked} where id = {303}"
                        sql.server.execute(update_time)
                        sql.engine.commit()

                        # update the workout in skill_sh
                        total_mission = int(get_total_workout() / 12)
                        update_mission = f"update skill_sh set mission_recall = {total_mission} where id = {303}"
                        sql.server.execute(update_mission)
                        sql.engine.commit()

                        # update the time in report_table
                        update_time_report = f"update report_time_recall set body = body + {worked} where cur_date = CURDATE()"
                        sql.server.execute(update_time_report)
                        sql.engine.commit()

                        # update the mission in report_table
                        update_mission_report = f"update report_mission_recall set body = body + {total_mission} where cur_date = CURDATE()"
                        sql.server.execute(update_mission_report)
                        sql.engine.commit()

                        # update the money
                        money_time = int(worked * 10000000)
                        update_money = f"update report_money set times = times + {money_time} where cur_date = CURDATE()"
                        sql.server.execute(update_money)
                        sql.engine.commit()

                        # update the money mission
                        money_mission = int(total_mission * 10000000)
                        update_money_mission = f"update report_money set mission = mission + {money_mission} where cur_date = CURDATE()"
                        sql.server.execute(update_money_mission)
                        sql.engine.commit()

                        # update in bank account
                        total_money_earned = int(money_mission + money_time)
                        money_update_bank = f"update game_bank set earned = earned + {total_money_earned} where account_id = 'onk'"
                        sql.server.execute(money_update_bank)
                        sql.engine.commit()

                        os.system(var.character_screen)
                    else:

                        workout_rep = int(input("\t\t ::: Rep: "))
                        print("")

                        print("")

                        key = {1: 'punch', 2: 'strike', 3: 'kick', 4: 'defense'}

                        # Add Count
                        add_count = f"update character_physiqe_sharp set {key.get(workout_id)} = {key.get(workout_id)} + {workout_rep} where cur_date = CURDATE()"
                        sql.server.execute(add_count)
                        sql.engine.commit()

                        # update total Count
                        fetch_total_count = "select SUM(punch + strike + kick + defense ) from character_physiqe_sharp where cur_date = CURDATE()"
                        sql.server.execute(fetch_total_count)
                        for x in sql.server:
                            total_count = int(x[0])

                        # update the totalCount
                        update_total_count = f"update character_physiqe_sharp set total_workout = {total_count} where cur_date = CURDATE()"
                        sql.server.execute(update_total_count)
                        sql.engine.commit()



                        print("\t ------- Workout Done ------- ")
                        os.system('cls')

            sharp()

        if option == 5:

            def silent():
                def hC(workout):
                    highest_count = f"select MAX({workout}) from character_physiqe_silent"
                    sql.server.execute(highest_count)
                    for x in sql.server:
                        high_count = int(x[0])

                    return high_count

                def tC(workout):
                    today_count = 0  # Default value
                    highest_count = f"select {workout} from character_physiqe_silent where cur_date = CURDATE()"
                    sql.server.execute(highest_count)
                    for x in sql.server:
                        today_count = int(x[0])

                    return today_count

                def get_total_workout():
                    fetch_total_count = "select total_workout from character_physiqe_silent where cur_date = CURDATE()"
                    sql.server.execute(fetch_total_count)
                    for x in sql.server:
                        total_workout = int(x[0])

                    return total_workout

                while True:
                    os.system('cls')
                    start_time = time.time()
                    print("--")

                    print(
                        "-------------------------------------------------------------------------------------------------------------------")
                    print("\t # Workout Reps: ", get_total_workout())
                    print("\t # Mission Done :", int(get_total_workout() / 12))
                    print(
                        "-------------------------------------------------------------------------------------------------------------------")
                    print("") # focus | breath | power
                    print(f"\t 1:: FOCUS : {tC('focus')}><{hC('focus')}")
                    print("")
                    print(f"\t 2:: BREATH : {tC('breath')}><{hC('breath')}")
                    print("")
                    print(f"\t 3:: POWER : {tC('power')}><{hC('power')}")
                    print("")

                    print(
                        "-------------------------------------------------------------------------------------------------------------------")
                    print("")
                    workout_id = int(input("\t\t ::: Workout ID: "))
                    if workout_id == 0:

                        end_time = time.time()
                        diff = int(end_time - start_time)
                        worked = int(diff / 60)

                        # update the workout in skill_sh
                        update_time = f"update skilL_sh set time_recall  = {worked} where id = {304}"
                        sql.server.execute(update_time)
                        sql.engine.commit()

                        # update the workout in skill_sh
                        total_mission = int(get_total_workout() / 12)
                        update_mission = f"update skill_sh set mission_recall = {total_mission} where id = {304}"
                        sql.server.execute(update_mission)
                        sql.engine.commit()

                        # update the time in report_table
                        update_time_report = f"update report_time_recall set body = body + {worked} where cur_date = CURDATE()"
                        sql.server.execute(update_time_report)
                        sql.engine.commit()

                        # update the mission in report_table
                        update_mission_report = f"update report_mission_recall set body = body + {total_mission} where cur_date = CURDATE()"
                        sql.server.execute(update_mission_report)
                        sql.engine.commit()

                        # update the money
                        money_time = int(worked * 10000000)
                        update_money = f"update report_money set times = times + {money_time} where cur_date = CURDATE()"
                        sql.server.execute(update_money)
                        sql.engine.commit()

                        # update the money mission
                        money_mission = int(total_mission * 10000000)
                        update_money_mission = f"update report_money set mission = mission + {money_mission} where cur_date = CURDATE()"
                        sql.server.execute(update_money_mission)
                        sql.engine.commit()

                        # update in bank account
                        total_money_earned = int(money_mission+money_time)
                        money_update_bank = f"update game_bank set earned = earned + {total_money_earned} where account_id = 'onk'"
                        sql.server.execute(money_update_bank)
                        sql.engine.commit()

                        os.system(var.character_screen)
                    else:

                        workout_rep = int(input("\t\t ::: Rep: "))
                        print("")

                        print("")

                        key = {1: 'focus', 2: 'breath', 3: 'power'}

                        # Add Count
                        add_count = f"update character_physiqe_silent set {key.get(workout_id)} = {key.get(workout_id)} + {workout_rep} where cur_date = CURDATE()"
                        sql.server.execute(add_count)
                        sql.engine.commit()

                        # update total Count
                        fetch_total_count = "select SUM(focus + breath + power ) from character_physiqe_silent where cur_date = CURDATE()"
                        sql.server.execute(fetch_total_count)
                        for x in sql.server:
                            total_count = int(x[0])

                        # update the totalCount
                        update_total_count = f"update character_physiqe_silent set total_workout = {total_count} where cur_date = CURDATE()"
                        sql.server.execute(update_total_count)
                        sql.engine.commit()

                        print("\t ------- Workout Done ------- ")
                        os.system('cls')

            silent()

        if option == 6:


            def fetch_account():
                fetch_account_info = "select * from game_bank"
                sql.server.execute(fetch_account_info)
                for x in sql.server:
                    acc_name = x[0]
                    acc_earned = (x[1]/10000000)
                    billion = int(acc_earned/80000000000)

                print(f"\t\t\t : {acc_name} - {number_to_inr(acc_earned)} Cr  -  ${billion} Bi")

            while True:
                os.system('cls')
                print("------------------------------------------------------------------------------------------------")
                print("\t ::: BANK :::")
                print("-------------------------------------------------------------------------------------------------")
                print("\t\t :: Accounts")
                fetch_account()
                print("-------------------------------------------------------------------------------------------------")

                view = int(input("View: "))

                if view == 0:
                    os.system(var.character_screen)
                else:
                    pass



