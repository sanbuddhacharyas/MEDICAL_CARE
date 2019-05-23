import gatt

from BLE import BLE

if __name__ == "__main__":

    manager = gatt.DeviceManager(adapter_name='hci0')
    device = BLE(manager=manager, mac_address='03:b3:ec:9a:97:b9')
    device.define_variables(21,167 ,"male",True, manager) # Age, Height , Gender
    device.connect()
    manager.run()
    device.body_composition()
    pass
