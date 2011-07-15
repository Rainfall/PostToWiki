#! /usr/bin/python

import pymongo
from pymongo import Connection

db = Connection().rtool
users = db.user
users.insert({"login":"Bob", "password":"123", "role":"0", "email":"bob@gmail.com"})
users.insert({"login":"Den", "password":"12345", "role":"1", "email":"den@gmail.com"})

def find_user(login, password):
        user_from_db = users.find_one({"login":login})
        if user_from_db is None:
            return None
        elif user_from_db["password"] == password:
            return True
        else:
            return False
