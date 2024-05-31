""" Importing Modules """
import pymongo

import urllib.parse

# Replace <password> with the actual password and ensure URL encoding
raw_password = "Asus15@9527"
encoded_password = urllib.parse.quote(raw_password, safe='')

# Now, `encoded_password` contains the URL-encoded password

#---------------------------------------------------------------------------------------------------------------------
class Con_mongodb:
    myclient = pymongo.MongoClient(f"mongodb+srv://OnkIndustries:{encoded_password}@onkcloud.8y9wfls.mongodb.net/")
    # creating a db variable to store the database
    # creating a table variable to store the collection


""" Creating Objects of the Con_mongodb """
mongo = Con_mongodb()
mongo_db = mongo.myclient['gbm']
mongo_cl = mongo_db['objectives']
mongo_cl2 = mongo_db['tasksReward']
