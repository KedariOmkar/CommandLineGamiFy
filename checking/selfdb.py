import sqlite3
# import pandas as pd
# import streamlit as st
# import sys
# import os
# sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")
from icecream import ic
#
# from src.common.common_constants import var
# from src.common.common_functions import number_to_inr, dayOngoing
# from src.database.mysql_connection import sql
#
#
# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor object
cur = conn.cursor()
#
# # # Create the table
# cur.execute('''
#     CREATE TABLE report_time_recall (
#         cur_date VARCHAR(20) PRIMARY KEY,
#         atma VARCHAR(30),
#         brain VARCHAR(30),
#         body VARCHAR(30),
#         lang INTEGER,
#         dsa INTEGER,
#         sub INTEGER,
#         tech INTEGER,
#         tools INTEGER,
#         build INTEGER,
#         softs INTEGER,
#         busi INTEGER,
#         total_time INTEGER
#     )
# ''')
#
# # Insert dummy data
# cur.execute("INSERT INTO report_time_recall VALUES ('2022-01-01', 1, 2, 3, 10, 20, 30, 40, 50, 60, 70, 80, 90)")
# cur.execute("INSERT INTO report_time_recall VALUES ('2022-01-02', 4, 5, 6, 20, 30, 40, 50, 60, 70, 80, 90, 100)")
# cur.execute("INSERT INTO report_time_recall VALUES ('2022-01-03', 7, 8, 9, 30, 40, 50, 60, 70, 80, 90, 100, 110)")
# cur.execute("INSERT INTO report_time_recall VALUES ('2022-01-04', 10, 11, 12, 40, 50, 60, 70, 80, 90, 100, 110, 120)")
# cur.execute("INSERT INTO report_time_recall VALUES ('2022-01-05', 13, 14, 15, 50, 60, 70, 80, 90, 100, 110, 120, 130)")
# cur.execute("INSERT INTO report_time_recall VALUES ('2022-01-06', 16, 17, 18, 60, 70, 80, 90, 100, 110, 120, 130, 140)")
# cur.execute("INSERT INTO report_time_recall VALUES ('2022-01-07', 19, 20, 21, 70, 80, 90, 100, 110, 120, 130, 140, 150)")
# cur.execute("INSERT INTO report_time_recall VALUES ('2022-01-08', 22, 23, 24, 80, 90, 100, 110, 120, 130, 140, 150, 160)")
# cur.execute("INSERT INTO report_time_recall VALUES ('2022-01-09', 25, 26, 27, 90, 100, 110, 120, 130, 140, 150, 160, 170)")
# cur.execute("INSERT INTO report_time_recall VALUES ('2022-01-10', 28, 29, 30, 100, 110, 120, 130, 140, 150, 160, 170, 180)")
#
# # print("Total sum of Lang:")
# # cur.execute('select sum(lang) from report_time_learn')
# # for x in cur:
# #     print(x[0])
# #
# # print("list of lang")
# # cur.execute('select lang from report_time_learn')
# # for x in cur:
# #     print(x[0])
# #
# # print("List of Dates")
# # cur.execute('select cur_date from report_time_learn')
# # for x in cur:
# #     print(x[0])
#
# # Commit the changes
# conn.commit()
#
# # Close the connection
# conn.close()
#
#
#
#
# def getTotalValueOfReport(column_name):
#     query = f"select sum({column_name}) from report_time_learn"
#     cur.execute(query)
#     for x in cur:
#         total_sum = int(x[0])
#
#     return total_sum
#
# def getFieldValue(column_name,table_name):
#     field_list = []
#     query = f"select {column_name} from {table_name}"
#     cur.execute(query)
#     for x in cur:
#         field_list.append(int(x[0]))
#
#     return field_list
#
# def getTotalValueForDay(total_column_name,table_name):
#     field_list = []
#     query = f"select {total_column_name} from {table_name}"
#     cur.execute(query)
#     for x in cur:
#         field_list.append(int(x[0]))
#
#     return field_list
#
# def getDateList(table_name):
#     field_list = []
#     query = f"select cur_date from {table_name}"
#     cur.execute(query)
#     for x in cur:
#         field_list.append(x[0])
#     return field_list
#
# # learn_time = getTotalValueForDay(table_name='report_time_learn',total_column_name='total_time')
# # recall_time = getTotalValueForDay(table_name='report_time_recall',total_column_name='total_time')
# # test_time = getTotalValueForDay(table_name='report_time_test',total_column_name='total_time')
# # ic(learn_time)
# # ic(recall_time)
# # ic(test_time)
#
# def plot_line_graph(table_name,field_name,table_title,label_x,label_y):
#     plot_data = pd.DataFrame({
#         label_x:getDateList(table_name),
#         label_y:getFieldList(field_name,table_name)
#     })
#
#     container = [
#         st.write(table_title),
#         st.line_chart(plot_data,x=label_x,y=label_y)
#     ]
#     return container
#
# #plot_line_graph('report_time_learn','lang','Time in Language','Dates','Time Learn')
import pandas as pd

from src.database.mysql_connection import sql

store_list_learn = []
cur.execute('select total_time from report_time_learn')
for x in cur:
    store_list_learn.append(x[0])

store_list_recall = []
cur.execute('select total_time from report_time_recall')
for x in cur:
    store_list_recall.append(x[0])


total_sum = [learn + recall  for learn, recall in zip(store_list_learn,store_list_recall)]
ic(store_list_learn)
ic(store_list_recall)
ic(total_sum)



def get_column_sum(table_name,column_name):
    query = f"select SUM({column_name}) from {table_name}"
    sql.server.execute(query)
    for x in sql.server:
        total_sum = int(x[0])
    return total_sum

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


ic(total_sum_count('time','total_time'))

ic(total_sum_count('mission','total_mission'))

def plot_line_graph(table_name,total_column_name,table_title,label_x,label_y):
    plot_data = pd.DataFrame({
        label_x:fetch_dates(table_name),
        label_y:(table_name,total_column_name)
    })

    container = [
        st.write(table_title),
        st.line_chart(plot_data,x=label_x,y=label_y)
    ]
    return container
