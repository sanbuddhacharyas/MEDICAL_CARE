import gatt
from login import *

from BLE import BLE

if __name__ == "__main__":
    root=Tk()
    #input_text=StringVar()
    user_name=StringVar()
    pass_word=StringVar()
    device = Database()
    localhost = 27017
    database = "Medicare_report"
    collections = "collection2"
    device.initialize(localhost ,database, collections)
    display = My_App(root,device)
    root.mainloop()


    # manager = gatt.DeviceManager(adapter_name='hci0')
    # device = BLE(manager=manager, mac_address='03:b3:ec:9a:97:b9')
    # device.define_variables(21,167 ,"male",True, manager) # Age, Height , Gender
    # device.connect()
    # manager.run()
    # device.body_composition()
    pass
