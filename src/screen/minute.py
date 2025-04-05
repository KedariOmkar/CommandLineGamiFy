import time
import winsound
import mysql.connector
from mysql.connector import Error
import signal
import sys


def cleanup_and_exit(signal, frame):
    global sql
    if sql and sql.is_connected():
        sql_db.close()
        sql.close()
        print("\nMySQL connection is closed")
    print("Program terminated gracefully")
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, cleanup_and_exit)

try:
    sql = mysql.connector.connect(
        host="localhost", user="root", password="root", database="gbm"
    )

    if sql.is_connected():
        # print("Connected to MySQL database")
        sql_db = sql.cursor()

        def beep_every_minute():
            frequency = 550  # Set Frequency To 1000 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second

            while True:
                try:
                    get_query = "select work_done from work_done_in_minutes;"
                    sql_db.execute(get_query)
                    for x in sql_db:
                        count = x[0]
                        hour = int(count / 60)
                    print("")
                    print(f"\rMinutes: {count} = {hour} Hr", end="")
                    winsound.Beep(frequency, duration)
                    # Update the count
                    query = "UPDATE work_done_in_minutes SET work_done = work_done + 1"
                    sql_db.execute(query)
                    sql.commit()

                except Error as e:
                    print(f"Error while updating the database: {e}")

                time.sleep(60)  # Wait for 60 seconds

        if __name__ == "__main__":
            beep_every_minute()

except Error as e:
    print(f"Error while connecting to the database: {e}")

finally:
    if sql.is_connected():
        sql_db.close()
        sql.close()
        print("MySQL connection is closed")
