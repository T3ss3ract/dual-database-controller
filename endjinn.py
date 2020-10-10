import os
import sys
import pyramid
import mysql.connector as mysql
import yaml
from pymongo import MongoClient
import tensorflow as tf

# set all sensitive data in a yaml config file
with open("config/config.yaml", "r") as conf:
    docs = yaml.load(conf, Loader=yaml.FullLoader)
    hhost = docs["host"]
    uuser = docs["user"]
    ppassword = docs["password"]
    ddatabase = docs["database"]
    mongo_dbname = docs["mgdb"]
    mongo_host = docs["mghost"]
    mongo_port = docs["mgport"]


client = MongoClient(mongo_host, mongo_port)
mgdb = client[mongo_dbname]
if mgdb is None:
    print("error connecting to mongodb")

# connect to database (DataBase Connection = dbc)
dbc = mysql.connect(host=hhost,
                    user=uuser,
                    password=ppassword,
                    database=ddatabase)

# if some error happens while connecting to mysql
if dbc is None:
    print("error! no database")
else:
    print(dbc.get_server_info())

# set values in the netUser table
def set_netUser(uname):
    return


# simple SELECT FROM WHERE select
# abstracted to the highest possible level.
# should be able to select anything from any table
def generic_mysql_sselect(table, selectparams, conditions):
    final_string = ""
    for i in selectparams:
        formatted_singleton = f"{i}, "
        final_string += formatted_singleton
    final_string = final_string[:-2] # remove last space and last comma
    # print(final_string)
    query = f""" 
        SELECT {final_string} FROM {table} WHERE {conditions}
    """
    print(query)
    csr = dbc.cursor()
    csr.execute(query)
    res = csr.fetchall()
    print(res)
    return res


def quick_mongo_migrate():
    return


def generic_mongodb_select(params):

    return



if __name__ == "__main__":
    print("tensorflow engine starting...")
    generic_mysql_sselect("employees", ("name", "dateHired", "empGroup"), "empGroup = \"Executives\"")
    dbc.close()
    vc = mgdb[mongo_dbname]
    for p in vc.find():
        print(p)
    client.close()