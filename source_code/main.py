import gatt
from login import *
import tkinter as tk
from tkinter import *
from functools import partial
from database import Database
from BLE import BLE
from UART import UART

if __name__ == "__main__":


    #BLE
    manager = gatt.DeviceManager(adapter_name='hci0')
    BIA = BLE(21,167 ,"male",True,manager=manager, mac_address='03:b3:ec:9a:97:b9')
    
    
    
    #Mongodb
    localhost = 27017
    database = "Medicare_report"
    collections = "collection2"
    device = Database(localhost ,database, collections)

    #Uart
    Uart = UART(9600, 21)

    
    #Tkinter
    root=Tk()
    display = My_App(root,device, Uart ,BIA)
    root.mainloop()
    
    pass
