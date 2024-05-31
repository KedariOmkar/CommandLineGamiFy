import sys
import os

sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")

from matplotlib import pyplot as plt

from src.common.common_constants import var
from src.common.common_functions import number_to_inr, dayOngoing
from src.database.mysql_connection import sql


from src.common.common_imports import *

# ----------------------------------------------------------------------------------------------------------------------


while True:
    os.system('cls')
    
    print("------------------------------------------------------------------------------------------------------------")
    print("\t # STATS")
    print("------------------------------------------------------------------------------------------------------------")
    print("\t  1. STATIC")
    print("\t  2. VISUAL")
    print("------------------------------------------------------------------------------------------------------------")
    
    option = int(input("\t Select: "))
    
    if option == 0:
        os.system(var.home_screen)
    else:
        
        if option == 1:

            #
            # def getCount(value,table,field_option,field_value,field_option_2,field_value_2):
            #     fetch_count = f"select COUNT({value}) from {table} where {field_option} = {field_value} and {field_option_2} = {field_value_2}"
            #     sql.server.execute(fetch_count)
            #     for x in sql.server:
            #         count = x[0]
            #
            # #getCount('id','skill_tg','field','lang','level','pro')
            #
            # def getTotal(total_value,table):
            #     fetch_total = f"select sum({total_value}) from {table}"
            #     sql.server.execute(fetch_total)
            #     for x in sql.server:
            #         total = x[0]
            #
            #     return total
            #
            # def megaTotal():
            #
            #     # Time
            #     learn_time = getTotal('total_time','report_time_learn')
            #     recall_time = getTotal('total_recall','report_time_recall')
            #     test_time = getTotal('total_test','report_time_test')
            #     total_time = int(learn_time+recall_time+test_time)
            #
            #     # mission
            #     learn_mission = getTotal('total_mission', 'report_mission_learn')
            #     recall_mission = getTotal('total_recall', 'report_mission_recall')
            #     test_mission = getTotal('total_test', 'report_mission_test')
            #     total_mission = int(learn_mission + recall_mission + test_mission)
            #
            #
            #     # routine
            #     routine_total = getTotal('total_routine','character_routine')
            #     habit_total = getTotal('total_habit','character_habit')
            #
            #     # physiqe
            #     total_shield = getTotal('total_workout','character_physiqe_shield')
            #     total_sharp = getTotal('total_workout', 'character_physiqe_sharp')
            #     total_silent = getTotal('total_workout', 'character_physiqe_silent')
            #
            #     # money
            #     total_money = getTotal('total_money','report_money')
            #
            #
            #
            #

            def money_stats():
                # Earned Money
                sql.server.execute("select SUM(total_money) from report_money")
                for x in sql.server:
                    earned_money = int(x[0] / 10000000)

                # Wasted Money
                days_passed = dayOngoing()
                # money wassted
                target_money = 40350000000

                money_earned_per_day = int((days_passed * target_money) / 10000000)

                money_wasted = int(money_earned_per_day - earned_money)

                print(f"\t\t - EARNED : {number_to_inr(earned_money)} Cr")
                print(f"\t\t - LOST   : {number_to_inr(money_wasted)} Cr")



            while True:
                os.system('cls')
                print("------------------------------------------------------------------------------------------------------------")
                print("\t # STATIC")
                print("------------------------------------------------------------------------------------------------------------")
                print(" ::: GAME :::")
                print("")
                print(" ::: CHARACTER :::")
                print("\t : MONEY ")
                money_stats()
                print("------------------------------------------------------------------------------------------------------------")
                
                ask = int(input(""))
                # game : total hours , total mission , total routine , total habits 
                # character : skills , powers , lifestyle
                # money : total money
                # owned : profiles

        if option == 2:
            def stats():

                """ This function is used to show the line graphs """

                def plot_line_graph(report_table, total_field):
                    # Making a list to store the points
                    store_points = []

                    # Making a list to store the dates
                    store_dates = []

                    fetch_dates = f"select cur_date from {report_table}"
                    sql.server.execute(fetch_dates)
                    for x in sql.server:
                        data_dates = x[0]
                        store_dates.append(data_dates)

                    """ Fetching the Points """

                    fetch_points = f"select {total_field} from {report_table}"
                    sql.server.execute(fetch_points)
                    for x in sql.server:
                        data_points = int(x[0])
                        store_points.append(data_points)

                    """ Plotting a Line Chart """

                    plt.figure(figsize=(12, 6))
                    plt.grid()
                    plt.plot(store_dates, store_points, marker='o', color='b')
                    plt.xticks(rotation=90)
                    plt.tight_layout()
                    plt.show()

                def plot_mission_line(report_table):
                    def fetch_data_points(column, report_table):
                        column_data = []
                        fetch_points = f"select {column} from {report_table}"
                        sql.server.execute(fetch_points)
                        for x in sql.server:
                            data_points = int(x[0])
                            column_data.append(data_points)

                        return column_data

                    # list which stores the dates
                    def fetch_dates():
                        store_dates = []
                        fetch_dates = f"select cur_date from {report_table}"
                        sql.server.execute(fetch_dates)
                        for x in sql.server:
                            data_dates = x[0]
                            store_dates.append(data_dates)
                        return store_dates

                    # Plotting the points on the graph
                    plt.plot(fetch_dates(), fetch_data_points('total_mission', 'report_mission_learn'), color='blue',
                             linestyle='-', marker='o', label='Learn')
                    plt.plot(fetch_dates(), fetch_data_points('total_mission', 'report_mission_recall'), color='red',
                             linestyle='-', marker='o', label='Recall')
                    plt.plot(fetch_dates(), fetch_data_points('total_mission', 'report_mission_test'), color='green',
                             linestyle='-', marker='o', label='Test')

                    plt.xticks(rotation=65)

                    # Add labels for the x and y axes
                    plt.xlabel('Dates')
                    plt.ylabel('Count')

                    # Add a title to the plot
                    plt.title('Total Mission Report')

                    # Display a legend
                    plt.legend()

                    # Show the plot
                    plt.grid(True)
                    plt.show()

                def plot_time_line(report_table):
                    def fetch_data_points(column, report_table):
                        column_data = []
                        fetch_points = f"select {column} from {report_table}"
                        sql.server.execute(fetch_points)
                        for x in sql.server:
                            data_points = int(x[0])
                            column_data.append(data_points)

                        return column_data

                    # list which stores the dates
                    def fetch_dates():
                        store_dates = []
                        fetch_dates = f"select cur_date from {report_table}"
                        sql.server.execute(fetch_dates)
                        for x in sql.server:
                            data_dates = x[0]
                            store_dates.append(data_dates)
                        return store_dates

                    # Plotting the points on the graph
                    plt.plot(fetch_dates(), fetch_data_points('total_time', 'report_time_learn'), color='blue',
                             linestyle='-',
                             marker='o', label='Learn')
                    plt.plot(fetch_dates(), fetch_data_points('total_time', 'report_time_recall'), color='red',
                             linestyle='-',
                             marker='o', label='Recall')
                    plt.plot(fetch_dates(), fetch_data_points('total_time', 'report_time_test'), color='green',
                             linestyle='-',
                             marker='o', label='Test')

                    plt.xticks(rotation=65)

                    # Add labels for the x and y axes
                    plt.xlabel('Dates')
                    plt.ylabel('Count')

                    # Add a title to the plot
                    plt.title('Time Report')

                    # Display a legend
                    plt.legend()

                    # Show the plot
                    plt.grid(True)
                    plt.show()

                def plot_mistake_line(report_table):

                    def fetch_data_points(column):
                        column_data = []
                        fetch_points = f"select {column} from {report_table}"
                        sql.server.execute(fetch_points)
                        for x in sql.server:
                            data_points = int(x[0])
                            column_data.append(data_points)

                        return column_data

                    # list which stores the dates
                    def fetch_dates():
                        store_dates = []
                        fetch_dates = f"select cur_date from {report_table}"
                        sql.server.execute(fetch_dates)
                        for x in sql.server:
                            data_dates = x[0]
                            store_dates.append(data_dates)
                        return store_dates

                    # Define the items and their equivalent labels and colors
                    items = ['pornstars', 'singers', 'actors', 'celebs', 'speakers', 'girlfriends', 'relatives',
                             'elites',
                             'comedians', 'influencers', 'youtubers']
                    labels = ['Pornstars', 'Singers', 'Actors', 'Celebs', 'Speakers', 'Girlfriends', 'Relatives',
                              'Elites',
                              'Comedians', 'Influencers', 'Youtubers']
                    colors = ['#000000', '#333333', '#191970', '#006400', '#8B0000', '#4B0082', '#800080', '#FFA500',
                              '#FF6347',
                              '#8A2BE2', '#4CAF50']

                    # Plotting the points on the graph
                    for item, label, color in zip(items, labels, colors):
                        plt.plot(fetch_dates(), fetch_data_points(item), marker='o', linestyle='-', color=color,
                                 label=label)

                    # Additional customization if needed
                    plt.xlabel('X-axis label')
                    plt.ylabel('Y-axis label')
                    plt.title('MATRIX AGETNS')
                    plt.legend()

                    # Show the plot
                    plt.show()

                def plot_session_line(report_table):

                    def fetch_data_points(column):
                        column_data = []
                        fetch_points = f"select {column} from {report_table}"
                        sql.server.execute(fetch_points)
                        for x in sql.server:
                            data_points = int(x[0])
                            column_data.append(data_points)

                        return column_data

                    # list which stores the dates
                    def fetch_dates():
                        store_dates = []
                        fetch_dates = f"select cur_date from {report_table}"
                        sql.server.execute(fetch_dates)
                        for x in sql.server:
                            data_dates = x[0]
                            store_dates.append(data_dates)
                        return store_dates

                    """
                    hex_colors = [
                '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
                '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5',
                '#393b79', '#e377c2', '#8c564b', '#7f7f7f', '#c49c94', '#17becf', '#aec7e8', '#ff7f0e', '#1f77b4', '#2ca02c'
            ]
                    """

                    # Plotting the points on the graph
                    plt.plot(fetch_dates(), fetch_data_points('a'), color='#1f77b4', linestyle='-', marker='o',
                             label='3:00 am')
                    plt.plot(fetch_dates(), fetch_data_points('b'), color='#ff7f0e', linestyle='-', marker='o',
                             label='3:30 am')
                    plt.plot(fetch_dates(), fetch_data_points('c'), color='#2ca02c', linestyle='-', marker='o',
                             label='4:10 am')
                    plt.plot(fetch_dates(), fetch_data_points('d'), color='#d62728', linestyle='-', marker='o',
                             label='4:30 am')
                    plt.plot(fetch_dates(), fetch_data_points('e'), color='#9467bd', linestyle='-', marker='o',
                             label='5:00 am')
                    plt.plot(fetch_dates(), fetch_data_points('f'), color='#8c564b', linestyle='-', marker='o',
                             label='6:00 am')
                    plt.plot(fetch_dates(), fetch_data_points('g'), color='#e377c2', linestyle='-', marker='o',
                             label='7:00 am')
                    plt.plot(fetch_dates(), fetch_data_points('h'), color='#7f7f7f', linestyle='-', marker='o',
                             label='8:00 am')
                    plt.plot(fetch_dates(), fetch_data_points('i'), color='#bcbd22', linestyle='-', marker='o',
                             label='9:00 am')
                    plt.plot(fetch_dates(), fetch_data_points('j'), color='#17becf', linestyle='-', marker='o',
                             label='10:00 am')
                    plt.plot(fetch_dates(), fetch_data_points('k'), color='#aec7e8', linestyle='-', marker='o',
                             label='11:00 am')
                    plt.plot(fetch_dates(), fetch_data_points('l'), color='#ffbb78', linestyle='-', marker='o',
                             label='12:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('m'), color='#98df8a', linestyle='-', marker='o',
                             label='1:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('n'), color='#ff9896', linestyle='-', marker='o',
                             label='2:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('o'), color='#c5b0d5', linestyle='-', marker='o',
                             label='3:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('p'), color='#c49c94', linestyle='-', marker='o',
                             label='4:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('q'), color='#f7b6d2', linestyle='-', marker='o',
                             label='5:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('r'), color='#c7c7c7', linestyle='-', marker='o',
                             label='6:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('s'), color='#dbdb8d', linestyle='-', marker='o',
                             label='7:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('t'), color='#9edae5', linestyle='-', marker='o',
                             label='8:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('u'), color='#393b79', linestyle='-', marker='o',
                             label='9:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('v'), color='#e377c2', linestyle='-', marker='o',
                             label='10:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('x'), color='#8c564b', linestyle='-', marker='o',
                             label='11:00 pm')
                    plt.plot(fetch_dates(), fetch_data_points('y'), color='#7f7f7f', linestyle='-', marker='o',
                             label='11:30 pm')
                    plt.plot(fetch_dates(), fetch_data_points('z'), color='#c49c94', linestyle='-', marker='o',
                             label='12:00 pm')

                    plt.xticks(rotation=65)

                    # Add labels for the x and y axes
                    plt.xlabel('Dates')
                    plt.ylabel('Count')

                    # Add a title to the plot
                    plt.title('CHARACTER ROUTINE')

                    # Display a legend
                    plt.legend()

                    # Show the plot
                    plt.grid(True)
                    plt.show()

                """ This Function is used to show the bar graphs """

                def plot_bar_graph_(report_table):
                    def fetch_field_count(field, report_table):
                        find_sum_query = f"select SUM({field}) from {report_table}"
                        sql.server.execute(find_sum_query)
                        for x in sql.server:
                            field_count = int(x[0])
                        return field_count

                    """ This are the points """

                    atma = fetch_field_count('atma', f'{report_table}')
                    brain = fetch_field_count('brain', f'{report_table}')
                    body = fetch_field_count('body', f'{report_table}')
                    lang = fetch_field_count('lang', f'{report_table}')
                    dsa = fetch_field_count('dsa', f'{report_table}')
                    sub = fetch_field_count('sub', f'{report_table}')
                    tech = fetch_field_count('tech', f'{report_table}')
                    tools = fetch_field_count('tools', f'{report_table}')
                    build = fetch_field_count('build', f'{report_table}')
                    softs = fetch_field_count('softs', f'{report_table}')
                    busi = fetch_field_count('busi', f'{report_table}')

                    y = (atma, brain, body, lang, dsa, sub, tech, tools, build, softs, busi)
                    x = ("ATMA", "BRAIN", 'BODY', 'LANW', 'DSA', 'SUB', 'TECH', 'TOOLS', 'BUILD', 'SOFTS', 'BUSI')

                    plt.bar(x, y)

                    plt.xticks(rotation=65)

                    # Add labels for the x and y axes
                    plt.xlabel('Fields')
                    plt.ylabel('Count')

                    # Add a title to the plot
                    plt.title('Report')

                    # Display a legend
                    plt.legend()

                    # Show the plot
                    plt.grid(True)
                    plt.show()

                def plot_bar_routine():
                    def fetch_field_count(field):
                        find_sum_query = f"select SUM({field}) from character_routine"
                        sql.server.execute(find_sum_query)
                        for x in sql.server:
                            field_count = int(x[0])
                        return field_count

                    """ This are the points """

                    a = fetch_field_count('a')
                    b = fetch_field_count('b')
                    c = fetch_field_count('c')
                    d = fetch_field_count('d')
                    e = fetch_field_count('e')
                    f = fetch_field_count('f')
                    g = fetch_field_count('g')
                    h = fetch_field_count('h')
                    i = fetch_field_count('i')
                    j = fetch_field_count('j')
                    k = fetch_field_count('k')
                    l = fetch_field_count('l')
                    m = fetch_field_count('m')
                    n = fetch_field_count('n')
                    o = fetch_field_count('o')
                    p = fetch_field_count('p')
                    q = fetch_field_count('q')
                    r = fetch_field_count('r')
                    s = fetch_field_count('s')
                    t = fetch_field_count('t')
                    u = fetch_field_count('u')
                    v = fetch_field_count('v')
                    x = fetch_field_count('x')
                    y = fetch_field_count('y')
                    z = fetch_field_count('z')

                    y = (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, x, y, z)
                    x = (
                    '3:00', '3:30', '4:10', '4:30', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00',
                    '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '11:30',
                    '12:00')

                    plt.bar(x, y)
                    plt.xticks(rotation=40)

                    plt.show()

                def plot_bar_mistakes():

                    def fetch_field_count(field):
                        find_sum_query = f"select SUM({field}) from game_matrix_agents"
                        sql.server.execute(find_sum_query)
                        for x in sql.server:
                            field_count = int(x[0])
                        return field_count

                    """ This are the points """

                    pornstars = fetch_field_count('pornstars')
                    actors = fetch_field_count('actors')
                    celebs = fetch_field_count('celebs')
                    speakers = fetch_field_count('speakers')
                    singers = fetch_field_count('singers')
                    girlfriends = fetch_field_count('girlfriends')
                    relatives = fetch_field_count('relatives')
                    elites = fetch_field_count('elites')
                    comedians = fetch_field_count('comedians')
                    influencers = fetch_field_count('influencers')
                    youtubers = fetch_field_count('youtubers')

                    y = (pornstars, singers, actors, celebs, speakers, girlfriends, relatives, elites, comedians,
                         influencers, youtubers)
                    x = ('Pornstars', 'Singers', 'Actors', 'Celebs', 'Speakers', 'Girlfriends', 'Relatives', 'Elites',
                         'Comedians', 'Influencers', 'Youtubers')

                    plt.bar(x, y)
                    plt.xticks(rotation=40)

                    plt.show()

                """ This function shows fields with learn - recall - fuckTe missions """

                def plot_grp_time(skill_table, field, title):
                    name_list = []
                    learn_list = []
                    recall_list = []
                    test_list = []

                    query = f"select * from {skill_table} where field = '{field}'"
                    sql.server.execute(query)
                    for x in sql.server:
                        id = x[0]
                        name = x[1]
                        learn = x[3]
                        recall = x[4]
                        test = x[5]

                        name_list.append(name)
                        learn_list.append(learn)
                        recall_list.append(recall)
                        test_list.append(test)

                    # Bar width
                    bar_width = 0.12

                    # Set the positions of the bars on the x-axis
                    r1 = range(len(learn_list))
                    r2 = [x + bar_width for x in r1]
                    r3 = [x + bar_width for x in r2]

                    # Create the bar graph
                    plt.bar(r1, learn_list, color='r', width=bar_width, edgecolor='black', label='Learn')
                    plt.bar(r2, recall_list, color='g', width=bar_width, edgecolor='black', label='Recall')
                    plt.bar(r3, test_list, color='b', width=bar_width, edgecolor='black', label='Test')

                    # Add a title
                    plt.title(title)

                    # Add legend
                    plt.legend()

                    # Customize the x-axis ticks and labels
                    plt.xticks([r + bar_width for r in range(len(learn_list))], name_list)

                    # Show the bar graph
                    plt.show()

                def plot_grp_mission(skill_table, field, title):
                    name_list = []
                    learn_list = []
                    recall_list = []
                    test_list = []

                    query = f"select * from {skill_table} where field = '{field}'"
                    sql.server.execute(query)
                    for x in sql.server:
                        id = x[0]
                        name = x[1]
                        learn = x[6]
                        recall = x[7]
                        test = x[8]

                        name_list.append(name)
                        learn_list.append(learn)
                        recall_list.append(recall)
                        test_list.append(test)

                    # Bar width
                    bar_width = 0.12

                    # Set the positions of the bars on the x-axis
                    r1 = range(len(learn_list))
                    r2 = [x + bar_width for x in r1]
                    r3 = [x + bar_width for x in r2]

                    # Create the bar graph
                    plt.bar(r1, learn_list, color='r', width=bar_width, edgecolor='black', label='Learn')
                    plt.bar(r2, recall_list, color='g', width=bar_width, edgecolor='black', label='Recall')
                    plt.bar(r3, test_list, color='b', width=bar_width, edgecolor='black', label='Test')

                    # Add a title
                    plt.title(title)

                    # Add legend
                    plt.legend()

                    # Customize the x-axis ticks and labels
                    plt.xticks([r + bar_width for r in range(len(learn_list))], name_list)

                    # Show the bar graph
                    plt.show()

                """ This function shows the money stats """
                def plot_line_total_money():
                    # Making a list to store the points
                    store_points = []

                    # Making a list to store the dates
                    store_dates = []

                    fetch_dates = f"select cur_date from report_money"
                    sql.server.execute(fetch_dates)
                    for x in sql.server:
                        data_dates = x[0]
                        store_dates.append(data_dates)

                    """ Fetching the Points """

                    fetch_points = f"select total_money from report_money"
                    sql.server.execute(fetch_points)
                    for x in sql.server:
                        data_points = int(x[0]/10000000)
                        store_points.append(data_points)

                    """ Plotting a Line Chart """

                    plt.figure(figsize=(12, 6))
                    plt.xlabel('Dates')
                    plt.ylabel('Crores')
                    plt.title('Money Earned')
                    plt.grid()
                    plt.plot(store_dates, store_points, marker='o', color='b')
                    plt.xticks(rotation=90)
                    plt.tight_layout()
                    plt.show()

                def CompetitionMoneyEarned():
                    # Making lists to store the points and dates for the first dataset
                    store_points_money = []
                    store_dates_money = []

                    # Fetching dates and points for the first dataset
                    fetch_dates_money = "select cur_date from report_money"
                    sql.server.execute(fetch_dates_money)
                    for x in sql.server:
                        data_dates_money = x[0]
                        store_dates_money.append(data_dates_money)

                    fetch_points_money = "select total_money from report_money"
                    sql.server.execute(fetch_points_money)
                    for x in sql.server:
                        data_points_money = int(x[0] / 10000000)
                        store_points_money.append(data_points_money)

                    # Making lists to store the points and dates for the second dataset
                    store_points_competition = []
                    store_dates_competition = []

                    # Fetching dates and points for the second dataset
                    fetch_dates_competition = "select cur_date from game_competition"
                    sql.server.execute(fetch_dates_competition)
                    for x in sql.server:
                        data_dates_competition = x[0]
                        store_dates_competition.append(data_dates_competition)

                    fetch_points_competition = "select total_money from game_competition"
                    sql.server.execute(fetch_points_competition)
                    for x in sql.server:
                        data_points_competition = int(x[0] / 10000000)
                        store_points_competition.append(data_points_competition)

                    # Plotting both datasets on the same graph
                    plt.figure(figsize=(12, 6))
                    plt.xlabel('Dates')
                    plt.ylabel('Crores')
                    plt.title('Money Earned')
                    plt.grid()
                    plt.plot(store_dates_money, store_points_money, label='Character Earned', marker='o', color='b')
                    plt.plot(store_dates_competition, store_points_competition, label='Competition Earned', marker='o',
                             color='r')
                    plt.xticks(rotation=90)
                    plt.legend()
                    plt.tight_layout()
                    plt.show()

                def plot_line_total_money_competition():
                    # Making a list to store the points
                    store_points = []

                    # Making a list to store the dates
                    store_dates = []

                    fetch_dates = f"select cur_date from game_competition"
                    sql.server.execute(fetch_dates)
                    for x in sql.server:
                        data_dates = x[0]
                        store_dates.append(data_dates)

                    """ Fetching the Points """

                    fetch_points = f"select total_money from game_competition"
                    sql.server.execute(fetch_points)
                    for x in sql.server:
                        data_points = int(x[0]/10000000)
                        store_points.append(data_points)

                    """ Plotting a Line Chart """

                    plt.figure(figsize=(12, 6))
                    plt.xlabel('Dates')
                    plt.ylabel('Crores')
                    plt.title('Money Earned')
                    plt.grid()
                    plt.plot(store_dates, store_points, marker='o', color='b')
                    plt.xticks(rotation=90)
                    plt.tight_layout()
                    plt.show()

                while True:
                    os.system('cls')

                    print("")
                    print(
                        "-----------------------------------------------------------------------------------------------------------")
                    print("\t# VISUAL STATS")
                    print(
                        "-----------------------------------------------------------------------------------------------------------")
                    print("\t:::: SKILL REPORT :-")
                    print("\t\t::: TIME :::")
                    print("\t\t\t 1[ LEARN ]    2[ RECALL ]    3[ TEST ]    111[ COMBINE ]")
                    print("\t\t::: MISSION  :::")
                    print("\t\t\t 4[ LEARN ]    5[ RECALL ]    6[ TEST ]    222[ COMBINE ]")
                    print("\t\t::: MONEY :::")
                    print("\t\t\t 7[ T EARNED ]   8[ T COMP EARNED ]  9[ WAR ]")
                    print("\t:::: CHARACTER :-")
                    print("\t\t\t 11[ T ROUTINE ]  444[ C ROUTINE ]  22[ T AGENTS ]  333[ C AGENTS]   ")
                    print("\t:::: Pillar Reports :-")
                    print("\t\t\t TW : 1[ LANG ]   2[ DSA ]   3[ SUB ]   4[ TECH ]   5[ TOOLS ]   6[ BUILD ]")
                    print("\t\t\t EN : 7[ SOFTS ]   8[ BUSI ]")
                    print("")
                    print(
                        "-----------------------------------------------------------------------------------------------------------")
                    print("")
                    view = input("\t! View - [ BAR ]  [ LINE ]  [ GRP ]: ")
                    print("")

                    if view == 'b':
                        graph = int(input("\t! Graph Id: "))

                        if graph == 1:
                            plot_bar_graph_('report_time_learn')
                        if graph == 2:
                            plot_bar_graph_('report_time_recall')
                        if graph == 3:
                            plot_bar_graph_('report_time_test')
                        if graph == 4:
                            plot_bar_graph_('report_mission_learn')
                        if graph == 5:
                            plot_bar_graph_('report_mission_recall')
                        if graph == 6:
                            plot_bar_graph_('report_mission_test')
                        if graph == 11:
                            plot_bar_graph_('report_session')
                        if graph == 22:
                            plot_bar_graph_('game_matrix_agents')

                        if graph == 0:
                            os.system(var.home_screen)

                    if view == 'l':
                        graph = int(input("Graph Id: "))

                        if graph == 1:
                            plot_line_graph('report_time_learn', 'total_time')

                        if graph == 2:
                            plot_line_graph('report_time_recall', 'total_time')

                        if graph == 3:
                            plot_line_graph('report_time_test', 'total_time')

                        if graph == 4:
                            plot_line_graph('report_mission_learn', 'total_mission')

                        if graph == 5:
                            plot_line_graph('report_mission_recall', 'total_mission')

                        if graph == 7:
                            plot_line_total_money()

                        if graph == 8:
                            plot_line_total_money_competition()

                        if graph == 9:
                            CompetitionMoneyEarned()


                        if graph == 3:
                            plot_line_graph('report_mission_test', 'total_mission')

                        if graph == 11:
                            plot_line_graph('character_routine', 'total_routine')

                        if graph == 22:
                            plot_line_graph('game_matrix_agents', 'total_agents_killed')

                        if graph == 111:
                            plot_time_line('report_time_learn')

                        if graph == 222:
                            plot_mission_line('report_mission_learn')

                        if graph == 333:
                            plot_mistake_line('game_matrix_agents')

                        if graph == 444:
                            plot_session_line('character_routine')

                    if view == 'g':

                        field_list = {1: 'lang', 2: 'dsa', 3: 'sub', 4: 'tech', 5: 'tools', 6: 'build', 7: 'softs',
                                      8: 'busi'}

                        title_list = {1: 'Language', 2: 'DSA', 3: 'Subjects', 4: 'Tech Domains', 5: 'Tools', 6: 'Tools',
                                      7: 'Softskills', 8: 'Business Skills'}

                        table_list = {1: 'skill_tg', 2: 'skill_tg', 3: 'skill_tg', 4: 'skill_tg', 5: 'skill_tg',
                                      6: 'skill_tg',
                                      7: 'skill_en', 8: 'skill_en', }

                        mission_or_time = int(input("Time(0) or Mission(1): "))

                        if mission_or_time == 0:
                            graph = int(input("\t! Graph ID: "))
                            plot_grp_time(table_list.get(graph), field_list.get(graph), title_list.get(graph))

                        if mission_or_time == 1:
                            graph = int(input("\t! Graph ID: "))
                            plot_grp_mission(table_list.get(graph), field_list.get(graph), title_list.get(graph))

                    if view == '0':
                        os.system(var.stats_screen)

            stats()
                