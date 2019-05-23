import gatt
import numpy as np
import time
import datetime

class BLE(gatt.Device):
    
    def define_variables(self, Age, Height, Gender, Write, manager):
        self.Age = Age
        self.Height = Height
        self.Gender = Gender
        self.Write = Write
        self.values = []
        self.ReadStatus = False
        self.Read = True
        self.count = 0
        self.manager = manager


    def Write_Bytes(self, c):
        #Write bytes to initiate communication
        magicBytes = [0xac, 0x02, 0xf7, 0x00, 0x00, 0x00, 0xcc, 0xc3]
        c.write_value(magicBytes)

        #write 2nd bytes to server
        magicBytes = [0xac, 0x02, 0xfa, 0x00, 0x00, 0x00, 0xcc, 0xc6]
        c.write_value(magicBytes)
        #Calculate offset for error checking bits
        Offset = self.Age + self.Height - 56
        
        #Sending Age and height with offset to server
        magicBytes = [0xac, 0x02, 0xfb, 0x01, self.Age, self.Height,  0xcc, Offset]
        c.write_value(magicBytes)
        
        #time.sleep(1)
        #Calculate offset for Present date
        now = datetime.datetime.now()
        #Write present date to server(scale)
        Offset = (now.year-1799) + now.month + now.day
        magicBytes = [0xac, 0x02, 0xfd, (now.year - 2000), now.month, now.day, 0xcc, Offset]
        c.write_value(magicBytes)
        
        #time.sleep(1)
        #Calculate offset for time
        now = datetime.datetime.now()
        Offset = now.hour + now.minute
        magicBytes = [0xac, 0x02, 0xfc, now.hour, now.minute, 56, 0xcc, Offset]
        c.write_value(magicBytes)
        
        #time.sleep(1)
        magicBytes = [0xac, 0x02, 0xfe, 0x06, 0x00, 0x00, 0xcc, 0xd0]
        c.write_value(magicBytes)
        
        #time.sleep(0.6)

    def body_composition(self):
        #Weight of person shifting higher bit by 8bit position to left and or with lower bit to get 16bit value
        
        weight =  float(((self.values[0][12] << 8) | self.values[0][13]) / 10) #. kg
        Fat = float (((self.values[0][18] << 8 ) | self.values[0][19])/ 10) #.% 
        Calorie = int((self.values[1][5] << 8) | self.values[1][6] ) #. kcal
        bone_mass = float(((self.values[1][7] << 8 ) | self.values[1][8]) / 10 ) #. kg
        water = float(((self.values[1][9] << 8) | self.values[1][10]) / 10) #.% body composition
        MetabolicAge = int(self.values[1][11]) #In years

        print ("weight ===================>" + str(weight) +".Kg")
        print ("Fat ======================>" + str(Fat) + "%")
        print ("Calorie ==================>" + str(Calorie) + "Kcal")
        print ("Bone_mass ================>" + str(bone_mass) + "Kg")
        print ("Water ====================>" + str(water) + "%")
        print ("MetabolicAge =============>" + str(MetabolicAge) + "years")
        
        return {"Weight" : weight, 
                "Fat" : Fat, 
                "Calorie" : Calorie, 
                "BoneMass": bone_mass, 
                "Water" : water , 
                "MetabolicAge" : MetabolicAge }
                
            
    def services_resolved(self):
        super().services_resolved()
        for s in self.services:
            if s.uuid == '0000ffb0-0000-1000-8000-00805f9b34fb': #services 0016
                for c in s.characteristics:
                    if (c.uuid == '0000ffb1-0000-1000-8000-00805f9b34fb') and (self.Write == True): #char 0017
                        self.Write_Bytes (c)
                        self.Write = False
                        print(c)
                        
                        #c.enable_notifications()
                    if c.uuid == '0000ffb2-0000-1000-8000-00805f9b34fb' and self.Read == True:
                        c.read_value()
                        c.enable_notifications()
                        print(c)
                        self.Read = False


                    
    def characteristic_value_updated(self, characteristic, value):
        print("Firmware version:", value)
        
        check = value[0] + value[1]       
        if check == 0:
            self.ReadStatus = True
            
        if len(value) == 20 and self.ReadStatus == True :
            if id(value) != id(self.values[0]):
                self.values.append(value)
                self.count = 1 + self.count
                if self.count == 2:
                    self.manager.stop()
                    self.count =0