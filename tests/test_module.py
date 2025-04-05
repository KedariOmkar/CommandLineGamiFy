import sys
import os
import psycopg2

import requests

sys.path.append("W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals")
# #
# from rich.console import Console
# from rich.table import Table
# from src.database.mysql_connection import sql
from icecream import ic

#
#
# console = Console()
#
#
# store_list = []
# # Call the data from the databse
# sql.server.execute("select * from skill_en")
# for x in sql.server:
#     store_list.append(x)
#
# ic(store_list)
#
# # Create a new table
# table = Table(title="Tech Genius Skills")
#
# # get columns from table
# column_names = []
# sql.server.execute("desc skill_en")
# for x in sql.server:
#     column_names.append(x[0])
#
# for column in column_names:
#     table.add_column(f"{column}",justify="center")
#
# for rows in store_list:
#     table.add_row(f"{rows[0]}",f"{rows[1]}",f"{rows[2]}",f"{rows[3]}",f"{rows[4]}",f"{rows[5]}",f"{rows[6]}",f"{rows[7]}",f"{rows[8]}",f"[link=https://www.sweettreats.com]Visit Website[/link]")
#
# # Print the table
# console.print(table)
#
# #
# # import psycopg2
# #
# # # Replace these with your Supabase database credentials
# # DB_HOST = "aws-0-ap-south-1.pooler.supabase.com"
# # DB_NAME = "dev_db"
# # DB_USER = "postgres.nkfwwmxxuxxnpgrqpjxg"
# # DB_PASSWORD = "[Asus15@9527]"  # Replace this with your actual password
# # DB_PORT = "6543"  # Use the port specified in the connection string
# #
# # # Establish a connection to the PostgreSQL database
# # try:
# #     connection = psycopg2.connect(
# #         host=DB_HOST,
# #         database=DB_NAME,
# #         user=DB_USER,
# #         password=DB_PASSWORD,
# #         port=DB_PORT
# #     )
# #     cursor = connection.cursor()
# #     print("Connected to the database successfully")
# #
# #     # Execute a simple query to verify the connection
# #     cursor.execute("SELECT version();")
# #     db_version = cursor.fetchone()
# #     print(f"PostgreSQL Database Version: {db_version}")
# #
# # except psycopg2.OperationalError as e:
# #     print(f"Failed to connect to the database: {e}")
# #
# # finally:
# #     if connection:
# #         cursor.close()
# #         connection.close()
# #         print("Connection closed.")

import os
from supabase import create_client, Client

url = "https://nkfwwmxxuxxnpgrqpjxg.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5rZnd3bXh4dXh4bnBncnFwanhnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyODM3OTc3MiwiZXhwIjoyMDQzOTU1NzcyfQ.019wNYjA51jRneaLQjA1CsDt9bF6deMHKeW0X-6bLOE"

supabase: Client = create_client(url, key)

# response = supabase.schema("dev_db").table("user_lifestyle_routine").select("*").execute()
#
# print(response)
#
# while True:
#     ask_option = int(input("Again: "))
#     if ask_option != 0:
#         reward_name = input("Enter Name: ")
#         reward_cat = input("Enter Cat: ")
#         reward_sub_cat = input("Enter Sub Cat: ")
#         reward_token = 250
#         reward_status = "lock"
#         user_bought_time = "null"
#         user_ref = 1
#         print("---")
#
#         # inserting into db
#         response = (
#             supabase.schema("dev_db")
#             .table("user_rewards")
#             .insert(
#                 {
#                     "reward_name": f"{reward_name}",
#                     "reward_cat": f"{reward_cat}",
#                     "reward_sub_cat": f"{reward_sub_cat}",
#                     "reward_token": f"{reward_token}",
#                     "reward_status": f"{reward_status}",
#                     "user_bought_time": f"{user_bought_time}",
#                     "user_ref": f"{user_ref}",
#                 }
#             )
#             .execute()
#         )
#
#         # now uploading the pics:
#         print(f"Inserting pics into {reward_name}")
#         insert_again = int(input("End: "))
#
#     else:
#       break


# reward_id
# reward_cat
# reward_sub_cat
# reward_token
# reward_status
# user_bought_time
# user_ref


# supabase.storage.create_bucket(
#   'avatars',
#   options={"public": True}
# )

# file = "C:\\Users\\kedar\\Downloads\\model.jpg"
# response = supabase.storage.from_('avatars').upload('model.jpg', file)

# Assuming you have already uploaded the file
# Replace 'images' with your bucket name and 'photo.jpg' with your file path/name
#
# file_path = 'model.jpg'  # The file path you used in the upload
# bucket_name = 'avatars'  # The bucket name
#
# # Get the public URL of the file
# response = supabase.storage.from_(bucket_name).get_public_url(file_path)
#
# if response:
#     print("Public URL:", response)
# else:
#     print("Error generating URL")


# Function to download and upload image from URL to Supabase bucket
def upload_image_from_url(image_url, bucket_name, folder_name, file_name):
    try:
        # Step 1: Download the image from URL
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content

            # Step 2: Upload the image to the specified folder in the bucket
            file_path = f'{folder_name}/{file_name}'
            upload_response = supabase.storage.from_(bucket_name).upload(file_path, image_data)

            print(upload_response)
            # Check for error in upload response
            # if upload_response("error"):  # Adjusted check for error
            #     raise Exception(f"Failed to upload image: {upload_response['error']['message']}")
            # else:
            #     print(f"Image uploaded successfully: {file_path}")
        else:
            raise Exception(f"Failed to download image, status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage: List of image URLs to download and upload
image_urls = [
    "https://www.carpixel.net/w/ff29f8ef1a5f1696db2ab934e7f89351/bmw-x5-m-competition-car-wallpaper-120857.jpg"
]

bucket_name = 'avatars'
folder_name = 'lavish'  # This folder will be automatically created in the bucket
row_id = 3

for idx, url in enumerate(image_urls):
    # You can customize file names here
    file_name = f"{row_id}.jpg"
    upload_image_from_url(url, bucket_name, folder_name, file_name)


# Function to retrieve public URLs for images in a folder
# def get_public_urls(bucket_name, folder_name, file_names):
#     public_urls = []
#     for file_name in file_names:
#         file_path = f'{folder_name}/{file_name}'
#         response = supabase.storage.from_(bucket_name).get_public_url(file_path)
#
#         if response:
#             public_urls.append(response)
#         else:
#             print(f"Error generating public URL for: {file_name}")
#     return public_urls
#
# # Example usage: List of file names you uploaded
# file_names = [
#     "image_1.jpg",
#     "image_2.jpg",
#     "image_3.jpg"
# ]
#
# bucket_name = 'avatars'
# folder_name = 'miamelano'  # Folder name where images are stored
#
# # Get public URLs for the images
# public_urls = get_public_urls(bucket_name, folder_name, file_names)
#
# # Print the public URLs
# for url in public_urls:
#     print(url)


# response = supabase.schema("dev_db").from_('user_enemies').select('*').execute()
# print(response)
# # Get the first item in the data list
