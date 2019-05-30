import serial 
import RPi.GPIO as GPIO

class UART():
    def __init__(self,baud,pin_num):
        GPIO.setmode(GPIO.BCM)
        self.ser = serial.Serial("/dev/ttyS0", baud)
        GPIO.setup(pin_num ,GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.setup(20,GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.add_event_detect(pin_num, GPIO.FALLING, callback = self.callback, bouncetime= 100)
        self.status = False
        

    def callback(self,channel):
        if self.status == False:
            self.data = []
        print("I am comming\n")
        while self.ser.inWaiting() > 0:
            received = self.ser.read()
            self.data.append(received.decode())
            print(received.decode())
        if self.data != []:
            self.status = True
    
    def write(self, data_num):
        self.ser.write(data_num.encode())





