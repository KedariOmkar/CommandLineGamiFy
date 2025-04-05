import sys
import os

sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")
from matplotlib import pyplot as plt
from src.common.common_constants import var
from src.common.common_functions import number_to_inr, dayOngoing
from src.database.mysql_connection import sql

import pandas as pd
import streamlit as st

from src.common.common_imports import *

# ---
# Function

def fetch_dates(table_name):
    """
    : param : str - table_name
    : return : list - of dates
    """
    list_of_dates = []
    query = f"select cur_date from {table_name}"
    sql.server.execute(query)
    for x in sql.server:
        list_of_dates.append(x[0])
    return list(list_of_dates)

def fetch_data_points(table_name,column_name):
    """
       ! Parameters:
            - table_name : str
            - column_name : str
       ! return : list - of dates
       """
    list_of_data_points = []
    query = f"select {column_name} from {table_name}"
    sql.server.execute(query)
    for x in sql.server:
        list_of_data_points.append(x[0])

    return list(list_of_data_points)

def total_sum_count(table_name_value,total_column_name):
    learn_count = fetch_data_points(f'report_{table_name_value}_learn', total_column_name)
    recall_count = fetch_data_points(f'report_{table_name_value}_recall', total_column_name)
    test_count = fetch_data_points(f'report_{table_name_value}_test', total_column_name)

    # Check if all lists have the same length
    #assert len(learn_count) == len(recall_count) == len(test_count), "Lists must have the same length"

    # Use zip to iterate over corresponding elements and sum them
    total_sum = [learn + recall + test for learn, recall, test in zip(learn_count, recall_count, test_count)]

    return total_sum

def fetch_data_points_total(table_name,total_column_name):
    """
       ! Parameters:
            - table_name : str
            - total_column_name : list(numbers)
       ! return : list - of total_values
       """
    list_of_total_data_points = []
    query = f"select {total_column_name} from {table_name}"
    sql.server.execute(query)
    for x in sql.server:
        list_of_total_data_points.append(x[0])

    return list(list_of_total_data_points)

def get_one_total_value(table_name1,table_name2,table_name3,total_column_name):

    total = []

    learn = fetch_data_points_total(table_name1,total_column_name)
    recall = fetch_data_points_total(table_name2,total_column_name)
    test = fetch_data_points_total(table_name3,total_column_name)

    total.extend(learn)
    total.extend(recall)
    total.extend(test)

    return total

def get_column_sum(table_name,column_name):
    query = f"select SUM({column_name}) from {table_name}"
    sql.server.execute(query)
    for x in sql.server:
        total_sum = int(x[0])
    return total_sum

def plot_bar_chart(table_name,table_title,label_x,label_y):

    """
    :param table_name: str - name of the table
    :param table_title: str - title for the chart
    :param label_x: str - label for the x-axis
    :param label_y: str - label for the y-axis
    :return: a complete chart
    """

    data = pd.DataFrame({
        label_x: ['Lang', 'Dsa', 'Sub', 'Tech', 'Tools','Build','Softs','Busi','Atma','Brain','Body'],
        label_y: [
            get_column_sum(table_name,'lang'),
            get_column_sum(table_name, 'dsa'),
            get_column_sum(table_name, 'sub'),
            get_column_sum(table_name, 'tech'),
            get_column_sum(table_name, 'tools'),
            get_column_sum(table_name, 'build'),
            get_column_sum(table_name, 'softs'),
            get_column_sum(table_name, 'busi'),
            get_column_sum(table_name, 'atma'),
            get_column_sum(table_name, 'brain'),
            get_column_sum(table_name, 'body'),
        ]
    })

    container = [
        st.write(table_title),
        st.bar_chart(data, x=label_x, y=label_y)
    ]
    return container

def plot_line_graph(table_name,total_column_name,table_title,label_x,label_y):
    plot_data = pd.DataFrame({
        label_x:fetch_dates(table_name),
        label_y:fetch_data_points_total(table_name,total_column_name)
    })

    container = [
        st.write(table_title),
        st.line_chart(plot_data,x=label_x,y=label_y)
    ]
    return container

def plot_bar_chart_routine(table_name,table_title,label_x,label_y):

    """
    :param table_name: str - name of the table
    :param table_title: str - title for the chart
    :param label_x: str - label for the x-axis
    :param label_y: str - label for the y-axis
    :return: a complete chart
    """

    data = pd.DataFrame({
        label_x: ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z'],
        label_y: [
            get_column_sum(table_name, 'a'),
            get_column_sum(table_name, 'b'),
            get_column_sum(table_name, 'c'),
            get_column_sum(table_name, 'd'),
            get_column_sum(table_name, 'e'),
            get_column_sum(table_name, 'f'),
            get_column_sum(table_name, 'g'),
            get_column_sum(table_name, 'h'),
            get_column_sum(table_name, 'i'),
            get_column_sum(table_name, 'j'),
            get_column_sum(table_name, 'k'),
            get_column_sum(table_name, 'l'),
            get_column_sum(table_name, 'm'),
            get_column_sum(table_name, 'n'),
            get_column_sum(table_name, 'o'),
            get_column_sum(table_name, 'p'),
            get_column_sum(table_name, 'q'),
            get_column_sum(table_name, 'r'),
            get_column_sum(table_name, 's'),
            get_column_sum(table_name, 't'),
            get_column_sum(table_name, 'u'),
            get_column_sum(table_name, 'v'),
            get_column_sum(table_name, 'x'),
            get_column_sum(table_name, 'y'),
            get_column_sum(table_name, 'z'),
        ]
    })

    container = [
        st.write(table_title),
        st.bar_chart(data, x=label_x, y=label_y)
    ]
    return container

def plot_bar_chart_workout(table_name,table_title,label_x,label_y):

    """
    :param table_name: str - name of the table
    :param table_title: str - title for the chart
    :param label_x: str - label for the x-axis
    :param label_y: str - label for the y-axis
    :return: a complete chart
    """


    data = pd.DataFrame({
        label_x: ['chest', 'back', 'shoulder', 'abs', 'leg', 'bicep', 'tricep', 'forearm'],
        label_y: [
            get_column_sum(table_name, 'chest'),
            get_column_sum(table_name, 'back'),
            get_column_sum(table_name, 'shoulder'),
            get_column_sum(table_name, 'abs'),
            get_column_sum(table_name, 'leg'),
            get_column_sum(table_name, 'bicep'),
            get_column_sum(table_name, 'tricep'),
            get_column_sum(table_name, 'forearm'),
        ]
    })

    container = [
        st.write(table_title),
        st.bar_chart(data, x=label_x, y=label_y)
    ]
    return container

def plot_bar_chart_mma(table_name,table_title,label_x,label_y):

    """
    :param table_name: str - name of the table
    :param table_title: str - title for the chart
    :param label_x: str - label for the x-axis
    :param label_y: str - label for the y-axis
    :return: a complete chart
    """


    data = pd.DataFrame({
        label_x:  ['punch', 'strike', 'kick', 'defense', 'attack'],
        label_y: [
            get_column_sum(table_name,'punch'),
            get_column_sum(table_name, 'strike'),
            get_column_sum(table_name, 'kick'),
            get_column_sum(table_name, 'defense'),
            get_column_sum(table_name, 'attack')
        ]
    })

    container = [
        st.write(table_title),
        st.bar_chart(data, x=label_x, y=label_y)
    ]
    return container

def plot_bar_chart_enemies(table_name,table_title,label_x,label_y):

    """
    :param table_name: str - name of the table
    :param table_title: str - title for the chart
    :param label_x: str - label for the x-axis
    :param label_y: str - label for the y-axis
    :return: a complete chart
    """

    data = pd.DataFrame({
        f"{label_x}":[
        'pornstars',
        'actors',
        'celebs',
        'speakers',
        'singers',
        'girlfriends',
        'relatives',
        'elites',
        'comedians',
        'influencers',
        'youtubers'
    ],
        f"{label_y}": [get_column_sum(table_name,'pornstars'),
                    get_column_sum(table_name,'actors'),
                    get_column_sum(table_name,'celebs'),
                    get_column_sum(table_name,'speakers'),
                    get_column_sum(table_name,'singers'),
                    get_column_sum(table_name,'girlfriends'),
                    get_column_sum(table_name,'relatives'),
                    get_column_sum(table_name,'elites'),
                    get_column_sum(table_name,'comedians'),
                    get_column_sum(table_name,'influencers'),
                    get_column_sum(table_name,'youtubers'),]
    })

    container = [
        st.write(table_title),
        st.bar_chart(data, x=label_x, y=label_y)

    ]
    return container

def plot_line_graph_total(table_name,table_name_value,total_column_name,table_title,label_x,label_y):
    plot_data = pd.DataFrame({
        label_x:fetch_dates(table_name),
        label_y:total_sum_count(table_name_value,total_column_name)
    })

    container = [
        st.write(table_title),
        st.line_chart(plot_data,x=label_x,y=label_y)
    ]
    return container


""" 
    Functions for Today's Game Statistics
"""


# ---------------------------------------------------------------------------------------------------------------------
""" Charts Starts From Here for the Complete Game """


st.header("Greatest Business Magnate")
st.write(f"Date:")


# Total
st.subheader("@ Total Game")
TotalTime , TotalMission = st.tabs(['Time','Mission'])

with TotalTime:
    plot_line_graph_total('report_time_learn','time','total_time','Time','Dates','Time Used')


with TotalMission:
    plot_line_graph_total('report_mission_learn', 'mission', 'total_mission', 'Mission', 'Dates', 'Mission Used')

# Time
st.subheader("Time")
LearnTime , RecallTime , TestTime = st.tabs(['Learn','Recall','Test'])

with LearnTime:
    plot_line_graph('report_time_learn','total_time','Time Learn','Dates','Time Count')

with RecallTime:
    plot_line_graph('report_time_recall','total_time','Recall Learn','Dates','Time Count')


with TestTime:
    plot_line_graph('report_time_test','total_time','Test Learn','Dates','Time Count')


# Mission
st.subheader("Mission")
LearnMission , RecallMission , TestMission = st.tabs(['Learn','Recall','Test'])

with LearnMission:
    plot_line_graph('report_mission_learn','total_mission','Mission Learn','Dates','Mission Count')


with RecallMission:
    plot_line_graph('report_mission_recall', 'total_mission', 'Mission Recall', 'Dates', 'Mission Count')

with TestMission:
    plot_line_graph('report_mission_test', 'total_mission', 'Mission Test', 'Dates', 'Mission Count')


st.write("---")

# Total Fields
st.header("@ Field")

st.subheader("Time")
LearnField , RecallField , TestField = st.tabs(['Learn','Recall','Test'])

with LearnField:
    plot_bar_chart('report_time_learn','Time Learn','Fields','Time Count')

with RecallField:
    plot_bar_chart('report_time_recall','Time Recall','Fields','Time Count')

with TestField:
    plot_bar_chart('report_time_test','Time Test','Fields','Time Count')


st.subheader("Missions")
LearnField , RecallField , TestField = st.tabs(['Learn','Recall','Test'])

with LearnField:
    plot_bar_chart('report_mission_learn','mission Learn','Fields','mission Count')

with RecallField:
    plot_bar_chart('report_mission_recall','mission Recall','Fields','mission Count')

with TestField:
    plot_bar_chart('report_mission_test','mission Test','Fields','mission Count')



st.header("@ Boosters")
st.subheader("Total")


routine_total , workout_total , mma_total , enemies_total = st.tabs(['Routine','Workout','MMA','Enemies'])

with routine_total:
    plot_line_graph('character_routine','total_routine','Routine','Dates','Routine Ticked')

with workout_total:
    plot_line_graph(' character_physiqe_shield','total_workout','Workout','Dates','Reps')

with mma_total:
    plot_line_graph(' character_physiqe_sharp','total_workout','Workout','Dates','Reps')

with enemies_total:
    plot_line_graph(' game_matrix_agents','total_agents_killed','Enemies','Dates','Got Killed')


st.subheader("Individual")

routine_individual , workout_individual , mma_individual , enemies_individual = st.tabs(['Routine','Workout','MMA','Enemies'])

with routine_individual:
    plot_bar_chart_routine('character_routine','Routine','Time','Ticked Times')

with workout_individual:
    plot_bar_chart_workout('character_physiqe_shield','Workout','Muscles','Reps Times')

with mma_individual:
    plot_bar_chart_mma('character_physiqe_sharp','Workout','Muscles','Reps Times')
#
with enemies_individual:
    plot_bar_chart_enemies('game_matrix_agents','Enemies','Enemies','Distracted Count')

