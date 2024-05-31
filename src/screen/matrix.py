import sys
import os

sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")
from src.common.common_functions import refresh_database
from src.database.mysql_connection import sql
from src.common.common_constants import *

# ---------------------------------------------------------------------------------------------------------------------

def number_to_inr(amount):
    formatted_amount = format_currency(amount,'INR',locale='en_IN')
    return formatted_amount

def get_sum(enemy_name):
    fetch_sum_enemy = f"SELECT SUM({enemy_name}) FROM game_matrix_agents"
    sql.server.execute(fetch_sum_enemy)
    got_sum = 0
    for x in sql.server:
        got_sum = int(x[0])
    return got_sum


def get_count(mistake_name):
    query = f"SELECT {mistake_name} FROM game_matrix_agents WHERE cur_date = CURDATE()"
    sql.server.execute(query)

    got_count = 0

    for x in sql.server:
        got_count = int(x[0])

    return got_count


def percentage_completion():
    sql.server.execute('select sum(total_agents_killed) from game_matrix_agents')
    for x in sql.server:
        total_agents_killed = x[0]

    return total_agents_killed



while True:
    os.system('cls')
    print("--")
    print("----------------------------------------------------------------------------------------------------------------")
    print(f"\t: MAYA CHOPPED DOWN  -- {int(percentage_completion()/var.target_agents_kill*100)}% ")
    print("----------------------------------------------------------------------------------------------------------------")
    print(f"\t :: Maya Detached : {get_sum('total_agents_killed')}  -- Time Saved: {get_sum('time_saved')} min / {int(get_sum('time_saved')/60)} hr")
    print(f"\t :: Maya Attached : {get_sum('total_agents_assult')}  -- Time Wasted: {get_sum('time_wasted')} min / {int(get_sum('time_wasted')/60)} hr")
    print("----------------------------------------------------------------------------------------------------------------")
    print("\t :: Maya Agents :: ")
    print(f"\t\t\t1. YOUTUBERS     #  {get_count('youtubers')}")
    print(f"\t\t\t2. CELEBRITIES   #  {get_count('celebs')}")
    print(f"\t\t\t3. ACTORS        #  {get_count('actors')}")
    print(f"\t\t\t4. SPEAKERS      #  {get_count('speakers')}")
    print(f"\t\t\t5. PORNSTARS     #  {get_count('pornstars')}")
    print(f"\t\t\t6. SINGERS       #  {get_count('singers')}")
    print(f"\t\t\t7. MODELS        #  {get_count('girlfriends')}")
    print(f"\t\t\t8. INFLUENCERS   #  {get_count('influencers')}")
    print(f"\t\t\t9. DREAMS        #  {get_count('relatives')}")
    print(f"\t\t\t10. COMEDIANS    #  {get_count('comedians')}")
    print("----------------------------------------------------------------------------------------------------------------")
    enemy = int(input("\t\t> Agent Id: "))


    if enemy == 0:
        os.system(var.home_screen)
    else:

        print("--")
        print("\t\t # Hare Krishna #")
        kill_thought = int(input("\t\t\t\t> Chop Them Down: "))
        print("\t\t # Hare Krishna #")
        print("--")
        time.sleep(1)
        if kill_thought == 1:

            ids = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,99]



            if enemy not in ids:
                pass
            else:
                enemy_dict = {1: 'youtubers', 2: 'celebs', 3: 'actors', 4: 'speakers', 5: 'pornstars', 6: 'singers',
                              7: 'girlfriends', 8: 'influencers', 9: 'relatives', 10: 'comedians'}

                time_saved = {'youtubers': 10, 'celebs': 10, 'actors': 30, 'speakers': 8, 'pornstars': 20, 'singers': 5,
                              'girlfriends': 20, 'influencers': 10, 'relatives': 2, 'comedians': 5}

                enemy_name = enemy_dict.get(enemy)

                if enemy == 99:
                    enemy_dict = {1: 'youtubers', 2: 'celebs', 3: 'actors', 4: 'speakers', 5: 'pornstars', 6: 'singers',
                                  7: 'girlfriends', 8: 'influencers', 9: 'relatives', 10: 'comedians'}

                    time_saved = {'youtubers': 10, 'celebs': 10, 'actors': 30, 'speakers': 8, 'pornstars': 20, 'singers': 5,
                                  'girlfriends': 20, 'influencers': 10, 'relatives': 2, 'comedians': 5}

                    # Update the Enemy Count
                    add_enemy_assult = f"update game_matrix_agents set total_agents_assult = total_agents_assult +  {1} where cur_date = CURDATE()"
                    sql.server.execute(add_enemy_assult)
                    sql.engine.commit()

                    # update the time wasted


                    # Add the Fine Count
                    enemy_assult_fine = f"update game_bank set fine = fine + {30000000} where account_id = 'ONK'"
                    sql.server.execute(enemy_assult_fine)
                    sql.engine.commit()

                    # update time wasted by killing the enemy
                    update_time_wasted = f"update game_matrix_agents set time_wasted = time_wasted + {25} where cur_date = CURDATE()"
                    sql.server.execute(update_time_wasted)
                    sql.engine.commit()

                    print(f"\t ## Fine : {number_to_inr(30000000)}")

                else:

                    enemy_dict = {1: 'youtubers', 2: 'celebs', 3: 'actors', 4: 'speakers', 5: 'pornstars', 6: 'singers',
                                  7: 'girlfriends', 8: 'influencers', 9: 'relatives', 10: 'comedians'}

                    time_saved = {'youtubers': 10, 'celebs': 10, 'actors': 30, 'speakers': 8, 'pornstars': 20, 'singers': 5,
                                  'girlfriends': 20, 'influencers': 10, 'relatives': 2, 'comedians': 5}


                    # Update the Enemy Count
                    add_enemy_count = f"update game_matrix_agents set {enemy_dict.get(enemy)} = {enemy_dict.get(enemy)} + 1 where cur_date = CURDATE()"
                    sql.server.execute(add_enemy_count)
                    sql.engine.commit()

                    # update time saved by killing the enemy
                    update_time_saved = f"update game_matrix_agents set time_saved = time_saved + {time_saved.get(enemy_name)} where cur_date = CURDATE()"
                    sql.server.execute(update_time_saved)
                    sql.engine.commit()

                    # Update the total Enemy Count
                    fetch_sum = "select SUM( youtubers + celebs + actors + speakers + pornstars + singers + girlfriends + influencers + relatives + comedians) from game_matrix_agents where cur_date = CURDATE()"
                    sql.server.execute(fetch_sum)
                    for x in sql.server:
                        total_sum = int(x[0])

                    # update the sum in total
                    update_total_sum = f"update game_matrix_agents set total_agents_killed = {total_sum} where cur_date = CURDATE()"
                    sql.server.execute(update_total_sum)
                    sql.engine.commit()


                    # Add the money Count
                    kill_money_earned = f"update game_bank set earned = earned + {10000000} where account_id = 'ONK'"
                    sql.server.execute(kill_money_earned)
                    sql.engine.commit()

                    refresh_database()

                    cash_collected = 10000000

                    print("")
                    print(f"\t :: Cash Collected: {number_to_inr(cash_collected)}")
                    time.sleep(1)

        else:
            enemy_dict = {1: 'youtubers', 2: 'celebs', 3: 'actors', 4: 'speakers', 5: 'pornstars', 6: 'singers',
                          7: 'girlfriends', 8: 'influencers', 9: 'relatives', 10: 'comedians'}

            time_saved = {'youtubers': 10, 'celebs': 10, 'actors': 30, 'speakers': 8, 'pornstars': 20, 'singers': 5,
                          'girlfriends': 20, 'influencers': 10, 'relatives': 2, 'comedians': 5}

            # Update the Enemy Count
            add_enemy_assult = f"update game_matrix_agents set total_agents_assult = total_agents_assult +  1 where cur_date = CURDATE()"
            sql.server.execute(add_enemy_assult)
            sql.engine.commit()

            # update the time wasted

            # Add the Fine Count
            enemy_assult_fine = f"update game_bank set fine = fine + {30000000} where account_id = 'ONK'"
            sql.server.execute(enemy_assult_fine)
            sql.engine.commit()

            # update time wasted by killing the enemy
            update_time_wasted = f"update game_matrix_agents set time_wasted = time_wasted + {25} where cur_date = CURDATE()"
            sql.server.execute(update_time_wasted)
            sql.engine.commit()

            print(f"\t ## Fine : {number_to_inr(30000000)}")




