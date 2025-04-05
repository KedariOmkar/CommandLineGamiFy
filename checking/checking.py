import pandas as pd
import streamlit as st
import sys
import os
sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")
from icecream import ic

from src.common.common_constants import var
from src.common.common_functions import number_to_inr, dayOngoing
from src.database.mysql_connection import sql





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


ic(get_column_sum('report_time_learn','lang'))

ic(get_one_total_value('report_time_learn','report_time_recall','report_time_test','total_time'))

# # Create a data frame
# data = pd.DataFrame({
#     'Dates': [1,2,3,4,5],
#     'Points':[1000,900,800,400,700]
# })
#
# # Create a line chart
# st.line_chart(data, x='X', y='Y')