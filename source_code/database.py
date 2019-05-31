from pymongo import MongoClient
import pymongo
from datetime import datetime

class Database():
    
    def __init__(self, localhost ,database, collections):
        self.client = MongoClient('localhost' , localhost  )
        self.db = self.client[database]
        self.coll = self.db[collections]
        self.User_database = {
                               "Height" : None,
<<<<<<< HEAD
                               "Systolic" : None,
                               "Diastolic" :None,
                               "HearBeat" : None,
                               "Temp" : None,
                               "Weight" : None, 
                                "Fat" : None, 
                                "Calorie" : None, 
                                "BoneMass": None, 
                                "Water" : None , 
                                "MAge" : None
=======
                               "Mage"   : None,
                               "Stolic" : None,
                               "Diastolic" :None,
                               "HearBeat" : None,
                               "Temp" : None,
>>>>>>> 46c6ccbaa747bef546d1d991583ef26dc12ee25c
                    
                              }
        self.User_id = None

    def DateDiff(self,d1,d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)
    
    def Register(self, Name, DOB):
        Name = Name.get()
        DOB  = DOB.get()
        print("Username" + Name)
        print("Username" + DOB)
        c = [i for i in self.coll.find({"$and":[{ 'Name' : Name} , {'DOB': DOB}]})]
        if c == []:
            l_user = self.coll.find().count()
            today_date = str(datetime.now().year)+"-"+str(datetime.now().month)+"-" + str(datetime.now().day)
            Age = int(self.DateDiff(today_date, DOB) /365)
            print("age" +str(Age))
            dic = {
                "Name" : Name,
                "Age" : Age,
                "DOB" : DOB,
                "User_id" : l_user,
                "info" : []
            }

            self.coll.insert_one(dic)
            print("Registered!!!")
            print("You User id "+str(l_user))
            return l_user

        else:
            print("Already exist")
    
    #Insert or update information of Username in info dictionary element
    def insert_info(self , health_info  ):  

        health_info.update({"Date": datetime.datetime.now()})
        self.coll.update({'User_id': self.User_id },{'$push' : { 'info':  health_info } })

    #def return_info(self):

    def Login(self, User_id):
        print('User_id'+User_id.get())
        c = [i for i in self.coll.find({"User_id": int(User_id.get()) })]
        if c != []:
            print("Name ====>"+str(c[0]["Name"]))
            print("Age  ====>"+str(c[0]["Age"]))
            print("DOB  ====>"+str(c[0]["DOB"]))
            print("User_id =>"+str(c[0]["User_id"]))
            self.User_id = User_id
            self.User_database = c[0]

        else:
            self.User_id = None
            self.User_database = None
    
    



    
