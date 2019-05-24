from pymongo import MongoClient
import pymongo

class Database():
    
    def initialize(self, localhost ,database, collections):
        self.client = MongoClient('localhost' , localhost  )
        self.db = self.client[database]
        self.coll = self.db[collections]
    
    def Register(self, Name, DOB, Age):
        c = [i for i in self.coll.find({"$and":[{ 'Name' : Name} ,{'Age' : Age} , {'DOB': DOB}]})]
        if c == []:
            l_user = self.coll.find().count()

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

       


    def Login(self, User_id):
        c = [i for i in self.coll.find({"User_id": User_id })]
        if c != []:
            print("Name ====>"+str(c[0]["Name"]))
            print("Age  ====>"+str(c[0]["Age"]))
            print("DOB  ====>"+str(c[0]["DOB"]))
            print("User_id =>"+str(c[0]["User_id"]))
            self.User_id = User_id

        else:
            print("Not registered yet")
    
    



    
