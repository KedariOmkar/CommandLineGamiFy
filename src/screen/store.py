
import sys
import os


sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")

import time
import subprocess
from src.common.common_constants import var
from src.common.common_functions import number_to_inr, get_date, terminate_application, open_browser
from src.database.mongodb_connection import mongo_cl
from src.database.mysql_connection import sql
from src.common.common_imports import *


# ---------------------------------------------------------------------------------------------------------------------


def availableAmount():
    fetchAvailable = "select earned from game_bank where account_id = 'ONK'"
    sql.server.execute(fetchAvailable)
    for x in sql.server:
        balance = int(x[0]/10000000)

    return balance

def fetchItems(ob_cat,ob_field):

    balance = int(availableAmount())

    fetch_items = f"select * from objectives where ob_cat = '{ob_cat}' and status = 'lock' and ob_field = '{ob_field}'"
    sql.server.execute(fetch_items)
    for x in sql.server:
        ob_id = x[0]
        ob_name = x[1]
        ob_cat = x[2]
        ob_sub_cat = x[3]
        ob_field = x[4]
        ob_price = int(x[5])
        ob_achieved_date = x[6]
        ob_age = x[7]
        ob_status = x[8]

        if ob_status == 'unlock':
            print(f"\t\t\t 🔓 - {ob_name.upper()} : {number_to_inr(ob_price)} Cr")
        else:
            print(f"\t\t\t 🔒 - {ob_name.upper()} : {number_to_inr(ob_price)} Cr")



def fetchLevel(item):
    fetch_level = f"select ob_price from objectives where ob_name = '{item}'"
    sql.server.execute(fetch_level)
    for x in sql.server:
        level = int(x[0])

    return level

def buyItem():
    print("--")
    item = input("\t Enter ob_name: ")
    print("--")


    # Fetch Item ob_name :
    def fetchDetails(item):
        view_item = f"select * from objectives where ob_name = '{item}'"
        sql.server.execute(view_item)
        for x in sql.server:
            ob_name = x[0]
            ob_cat = x[1]
            ob_field = x[2]
            level = x[3]
            price = x[4]
            status = x[5]
            bought_date = x[6]

            print("--")
            print(f"\t Balance: {number_to_inr(availableAmount())} Cr")
            print("--")
            print(f"\t ob_name : {x[0]}")
            print(f"\t Price : {number_to_inr(x[4]/10000000)} Cr")
            print(f"\t Unlock : {number_to_inr(x[3]/10000000)} Cr")
            print("--")


        buy = int(input("\t :: Confirm Buy: "))

        if buy == 1:
            print(" :: TRANSACTION :: ")
            pin = input("\t ! Enter Pin: ")
            if pin == 'onk':
                print("")

                balance_available = int(availableAmount() * 100000000)

                # insert into transaction
                insert_transaction = f"INSERT INTO game_bank_transaction (transaction_date, item_name, item_price, item_ob_cat, item_sub_ob_cat , balance_available , status) VALUES ('{get_date()}', '{item}', '{price}', '{ob_cat}', '{ob_field}',{balance_available},'success')"
                sql.server.execute(insert_transaction)
                sql.engine.commit()

                remaining = int(balance - price)

                # deduct balance from account
                deduct_amount = f"update game_bank set earned = {remaining} where account_id = 'ONK'"
                sql.server.execute(deduct_amount)
                sql.engine.commit()

                # update the item
                update_status = f"UPDATE objectives SET status = 'owned', bought_date = '{get_date()}' WHERE ob_name = '{item}'"
                sql.server.execute(update_status)
                sql.engine.commit()


                print(" :: TRASANCTION COMPLETED ::")
                print("")
                print("\t\t ::: Item Bought :::")
                time.sleep(5)

                def view_images(ob_name):
                    result = mongo_cl.find_one({"ob_name": item})

                    pics_list = []
                    if result:
                        pics = result.get('pics', [])
                        pics_list.extend(pics)

                        if pics_list:
                            # Construct the command to open all links in Firefox
                            firefox_executable = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                            command = [firefox_executable]
                            command.extend(pics_list)

                            # Run the command
                            browser_process = subprocess.Popen(command)

                            # Wait for user input to close the browser
                            while True:
                                user_input = input("Quit: ")
                                if user_input.lower() == 'q':
                                    # Terminate the browser process
                                    terminate_application('msedge.exe')
                                    break
                                else:
                                    print("Invalid input. Press 'q' to close the browser.")
                        else:
                            print("No pics found.")
                view_images(item)

            else:
                print("wrong pin...")

    def checkLevel(item):
        # fetch bank balance
        fetch_earned_money = "select earned from game_bank where account_id = 'ONK'"
        sql.server.execute(fetch_earned_money)
        for x in sql.server:
            global balance
            balance = int(x[0])

        level = fetchLevel(item)

        if balance > level:
            os.system('cls')

            fetchDetails(item)

        else:
            print("..Aukat Madorchod..")

            # Display the detaisl

    checkLevel(item)


def bought():

    def fetchBoughtItems(ob_cat,ob_field):
        fetch_items = f"select * from objectives where ob_cat = '{ob_cat}' and ob_field = '{ob_field}' and status = 'owned'"
        sql.server.execute(fetch_items)
        for x in sql.server:
            ob_name = x[0]
            price = int(x[4] / 10000000)

            print(f"\t\t\t 🔓 - {ob_name.upper()} : {number_to_inr(price)} Cr")

    def viewBoughtItems():
        print("--")
        view = input("\t :: View: ")

        bought_list = []

        fetch_bought_items = "select ob_name from objectives where status = 'owned'"
        sql.server.execute(fetch_bought_items)
        for x in sql.server:
            bought_list.append(x[0])

        if view not in bought_list:
            print("\t Not Owned..")
        else:
            result = mongo_cl.find_one({"ob_name": view})

        print("\t Opening Pics...")
        pics_list = []
        if result:
            pics = result.get('pics', [])
            pics_list.extend(pics)

            if pics_list:
                open_browser(pics_list)
                os.system(var.store_screen)
            else:
                print("No pics found.")

    while True:
        os.system('cls')
        print("------------------------------------------------------------------------------------------------------------")
        print(f"  :: OBJECTIVES ::")
        print("-------------------------------------------------------------------------------------------------------------")
        print("\t :: CORE")
        print("\t\t :: PROFILE")
        fetchBoughtItems('core', 'profile')
        print("\t\t :: INTRO")
        fetchBoughtItems('core', 'intro')
        print("")
        print("\t :: ASSET")
        print("\t\t :: COMPANY")
        fetchBoughtItems('asset', 'company')
        print("\t\t :: PROPERTIES")
        fetchBoughtItems('asset', 'properties')
        print("\t\t :: INVESTMENT")
        fetchBoughtItems('asset', 'investment')
        print("")
        print("\t :: LAVISH")
        print("\t\t :: HOUSE")
        fetchBoughtItems('lavish', 'house')
        print("\t\t :: CAR")
        fetchBoughtItems('lavish', 'car')
        print("\t\t :: ULTRA")
        fetchBoughtItems('lavish', 'ultra')
        print("\t\t :: LIFESTYLE")
        fetchBoughtItems('lavish', 'lifestyle')
        print("\t\t :: SOCIAL")
        fetchBoughtItems('lavish', 'social')
        print("")
        print("\t :: LIFE")
        print("\t\t :: RELATIONS")
        fetchBoughtItems('life', 'relation')
        print("------------------------------------------------------------------------------------------------------------")
        print(" : OPTIONS :   1.VIEW")
        option = int(input(" : Choose : "))

        if option == 0:
            os.system(var.store_screen)
    
        if option == 1:
            viewBoughtItems()

def editObjective():
    while True:
        print("--")
        ob_id_to_edit = input("\t Enter Id: ")
        print("--")

        # Fetch the current details of the objective
        fetch_details_query = f"SELECT * FROM objectives WHERE ob_id = {ob_id_to_edit}"
        sql.server.execute(fetch_details_query)
        objective_details = sql.server.fetchone()

        if not objective_details:
            print("\t Objective not found.")
            return

        ob_name = objective_details[1]
        ob_cat = objective_details[2]
        ob_sub_cat = objective_details[3]
        ob_field = objective_details[4]
        ob_price = objective_details[5]
        ob_achieved_date = objective_details[6]
        ob_age = objective_details[7]
        ob_status = objective_details[8]

        print(f"\t! Current details of Id - {ob_id_to_edit}:")
        print(f"\t! Name: {ob_name}")
        print(f"\t! Category: {ob_cat}")
        print(f"\t! Sub-Category: {ob_sub_cat}")
        print(f"\t! Field: {ob_field}")
        print(f"\t! Price: {ob_price}")
        print(f"\t! Achieved Date: {ob_achieved_date}")
        print(f"\t! Age: {ob_age}")
        print(f"\t! Status: {ob_status}")

        print("--")
        # Get new values from the user
        new_ob_name = input("\t# Enter Name: ").strip() or ob_name
        new_ob_cat = input("\t# Enter Category: ").strip() or ob_cat
        new_ob_sub_cat = input("\t# Enter Sub Cat: ").strip() or ob_sub_cat
        new_ob_field = input("\t# Enter Field: ").strip() or ob_field

        # Handle the input for price
        new_ob_price = input("\t# Enter Price: ").strip()
        new_ob_price = int(new_ob_price) if new_ob_price.isdigit() else ob_price


        new_ob_achieved_date = input("\t# Enter Date Achieved: ").strip() or ob_achieved_date

        # Handle the input for age
        new_ob_age = input("\t# Enter Age: ").strip()
        new_ob_age = int(new_ob_age) if new_ob_age.isdigit() else ob_age


        new_ob_status = input("\t# Enter Status: ").strip() or ob_status

        # Update the record in the database
        update_query = f"UPDATE objectives SET ob_name = '{new_ob_name}',ob_cat = '{new_ob_cat}',ob_sub_cat = '{new_ob_sub_cat}',ob_field = '{new_ob_field}',ob_price = {new_ob_price},ob_achieved_date = '{new_ob_achieved_date}',ob_age = {new_ob_age},status = '{new_ob_status}' WHERE ob_id = {ob_id_to_edit}"
        sql.server.execute(update_query)
        sql.engine.commit()

        print("\t ::: Successfully Updated :::")


def unlockObjective():
    print("--")
    ob_id_to_unlock = input("\t Enter ob_id to unlock: ")
    print("--")

    # Fetch the current details of the objective
    fetch_details_query = f"SELECT * FROM objectives WHERE ob_id = {ob_id_to_unlock}"
    sql.server.execute(fetch_details_query)
    objective_details = sql.server.fetchone()

    if not objective_details:
        print("\t Objective not found.")
        return

    ob_name = objective_details[1]
    ob_cat = objective_details[2]
    ob_sub_cat = objective_details[3]
    ob_field = objective_details[4]
    ob_price = objective_details[5]
    ob_achieved_date = objective_details[6]
    ob_age = objective_details[7]
    ob_status = objective_details[8]

    print(f"\t# Id: {ob_id_to_unlock}:")
    print(f"\t# Name: {ob_name}")
    print(f"\t# Category: {ob_cat}")
    print(f"\t# Sub-Category: {ob_sub_cat}")
    print(f"\t# Field: {ob_field}")
    print(f"\t# Price: {ob_price}")
    print(f"\t# Achieved Date: {ob_achieved_date}")
    print(f"\t# Age: {ob_age}")
    print(f"\t# Status: {ob_status}")

    if ob_status == 'unlock':
        print("\t Objective is already unlocked.")
        return

    print("--")
    # Confirm unlocking
    confirmation = int(input("\t Unlock Objective: "))

    if confirmation == 1:
        # Update the status to 'unlock' in the database
        update_query = f"UPDATE objectives SET status = 'unlock' WHERE ob_id = {ob_id_to_unlock}"
        sql.server.execute(update_query)
        sql.engine.commit()

        print("\t Objective unlocked successfully.")
    else:
        print("\t Unlocking canceled.")

# Add this function call where needed in your script.
# For example, you can call it in the main loop with an additional option.


# Add this function call where needed in your script.
# For example, you can call it in the main loop with an additional option.


def viewItem():
    print("--")
    view = input("\t :: View: ")
    check_item = f"select ob_price from objectives where ob_name = '{view}'"
    sql.server.execute(check_item)
    for x in sql.server:
        price = int(x[0])

    balance = availableAmount()

    if balance > price:
        view_item = f"select * from objectives where ob_name = '{view}'"
        sql.server.execute(view_item)
        for x in sql.server:
            print("--")
            print(f"\t Name : {x[1].upper()}")
            print(f"\t Price : {number_to_inr(int(x[5]))}")
            print("--")
            # Use find_one if you expect only one document
            result = mongo_cl.find_one({"ob_name": x[1]})

            pics_list = []
            if result:
                pics = result.get('pics', [])
                pics_list.extend(pics)

                if len(pics_list) >=1:
                    # Construct the command to open all links in Firefox
                    print("\t! Opening Browser")
                    open_browser(pics_list)
                    os.system(var.store_screen)
                else:
                    print("No pics found.")

    else:
        print("\t No Access.....")
        time.sleep(2)

def insert_into_mongodb(name, pic_urls):
    mongo_cl.update_one({"ob_name": name}, {"$set": {"pics": pic_urls}}, upsert=True)

def addNewObjective():
    print("--")
    ob_name = input("\t Enter Name: ").strip()
    ob_cat = input("\t Enter Cat: ").strip()
    ob_sub_cat = input("\t Enter Sub Cat: ").strip()
    ob_field = input("\t Enter Field: ").strip()
    ob_price = int(input("\t Enter Price: ").strip())
    ob_achieved_date = "null"
    ob_age = 0
    ob_status = "lock"
    print("--")

    # Insert the new objective into the database
    insert_query = f"INSERT INTO objectives (ob_name, ob_cat, ob_sub_cat, ob_field, ob_price, ob_achieved_date, ob_age, status) VALUES ('{ob_name}', '{ob_cat}', '{ob_sub_cat}', '{ob_field}', {ob_price}, '{ob_achieved_date}', {ob_age}, '{ob_status}')"

    try:
        sql.server.execute(insert_query)
        sql.engine.commit()
        print("\t Record Entered Successfully")
        print("-- Now Pics --")
        # Input and insert pictures into MongoDB
        pic_urls = []
        pic_input = 1
        while pic_input:
            pic_url = input(f"\t\t! PIC-{pic_input+1}: ")
            pic_urls.append(pic_url)
            pic_input = int(input("\t\t\t -- Again: "))

        insert_into_mongodb(ob_name, pic_urls)
        print("")
        print("\t :: Images Inserted Successfully ::")

    except Exception as e:
        print("\t Error adding objective:", e)


while True:
    os.system('cls')
    print("------------------------------------------------------------------------------------------------------------")
    print(f"  :: TARGETS ::")
    print(f"   : Balance - {(number_to_inr(availableAmount()))} Cr")
    print("-------------------------------------------------------------------------------------------------------------")

    print("\t :: PROFESSIONAL")
    print("\t\t :: Positions")
    fetchItems('positions','professional')
    print("\t\t :: Tags")
    fetchItems('tags','professional')
    print("")

    print("\t :: FINANCIAL")
    print("\t\t :: COMPANIES ")
    fetchItems('companies', 'financial')
    print("\t\t :: INVESTMENTS")
    fetchItems('investments', 'financial')
    print("\t\t :: LIQUID")
    fetchItems('liquid', 'financial')
    print("")

    print("\t :: LAVISH")
    print("\t\t :: MANSIONS ")
    fetchItems('mansions', 'lavish')
    print("\t\t :: CARS")
    fetchItems('cars', 'lavish')
    print("\t\t :: Ultra")
    fetchItems('ultra', 'lavish')
    print("\t\t :: LIFESTYLE")
    fetchItems('lifestyle', 'lavish')
    print("\t\t :: HOE")
    fetchItems('hoe', 'lavish')
    print("")

    print("\t :: PERSONAL")
    print("\t\t :: SELF ")
    fetchItems('self', 'personal')
    print("\t\t :: Parents")
    fetchItems('parents', 'personal')
    print("\t\t :: Relations")
    fetchItems('relations', 'personal')
    print("")

    print("\t :: PHILANTHROPIC")
    print("\t\t ::  FOOD ")
    fetchItems('food', 'philanthropic')
    print("\t\t ::  EDUCATION ")
    fetchItems('education', 'philanthropic')
    print("\t\t ::  GLOBAL ")
    fetchItems('global', 'philanthropic')
    print("------------------------------------------------------------------------------------------------------------")
    print(" : OPTIONS :   1[VIEW]    2[UNLOCK]    3[EDIT]    4[ADD]")
    option = int(input(" : Choose : "))

    if option == 0:
        os.system(var.home_screen)

    if option == 1:
        viewItem()

    if option == 2:
        unlockObjective()

    if option == 3:
        editObjective()

    if option == 4:
        addNewObjective()

