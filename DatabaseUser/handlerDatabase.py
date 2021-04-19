from server import *
from threading import Thread
from Message.request import Request
from DatabaseUser.objectUser import UserObj
import json

class HandlerDatabase():
   databaseFile = 'DatabaseUser/database.json'
   database = {}

   @staticmethod
   def addNewObj(obj):
      value = {
         "name" : obj.name,
         "phone": obj.phone,
         "pokemon" : obj.pokemon
      }

      try:
         with open(HandlerDatabase.databaseFile, 'r+') as file:
            HandlerDatabase.database = json.load(file)
            HandlerDatabase.database["usersObj"].append(value)
            file.seek(0)
            json.dump(HandlerDatabase.database, file)
            return "200"
      except:
         return "500"