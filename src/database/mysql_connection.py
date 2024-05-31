import sys

sys.path.append('W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals')

""" Importing Modules """
import mysql.connector

""" Class for Connecting to the Mysql Database """

# ----------------------------------------------------------------------------------------------------------------------

class Connect_mysql:
    engine = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="gbm"
    )

    server = engine.cursor()


""" Creating object of the Connect_mysql """
sql = Connect_mysql()




