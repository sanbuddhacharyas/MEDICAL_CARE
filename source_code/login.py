import tkinter as tk
import imageio
from tkinter import *
from functools import partial
from database import Database
from PIL import Image,ImageTk
import numpy as np
import time



class curry:
    def __init__(self, fun, *args, **kwargs):
        self.fun = fun
        self.pending = args[:]
        self.kwargs = kwargs.copy()

    def __call__(self, *args, **kwargs):
        if kwargs and self.kwargs:
            kw = self.kwargs.copy()
            kw.update(kwargs)
        else:
            kw = kwargs or self.kwargs

        return self.fun(*(self.pending + args), **kw)

# ---------- code for class: curry (end) ---------------------


# ---------- code for function: event_lambda (begin) --------
def event_lambda(f, *args, **kwds ):
    return lambda event, f=f, args=args, kwds=kwds : f( *args, **kwds )
# ---------- code for function: event_lambda (end) -----------


    



class My_App():
    def __init__(self,master,database_id, Uart ,BIA):
        self.expression=None
        self.master=master #instance of the Tk library
        pad=3
        self.database_id = database_id
        self.Uart = Uart
        self.BIA =  BIA
        self._geom='1024x800'
        self.master.geometry("{0}x{1}+0+0".format(
            self.master.winfo_screenwidth()-pad, self.master.winfo_screenheight()-pad))
        self.master.bind('<Escape>',self.toggle_geom)
        self.master.title("Selcouth Health")
        self.images = []
        for i in range(5):
            self.images.append(Image.open('GUIS/Loading_Screens/'+str(i)+'.jpg' ))

        #np.save("loading.npy", images)
        #print("images saved")
            
        

        # creating the container for the initial screen
        self.my_container1=Frame(self.master,bg='cadetblue4')
        self.my_container1.pack(expand='yes',fill=BOTH)

        #label on the top of the screen
        label_text='Choose Login Or Register'
        self.label1=Label(
                        self.my_container1,text=label_text,
                        bg='dark khaki',width='50',
                        height='2',font=('Calibri',14)
                        )
        self.label1.pack(side='top')
        #button widgets

        #widget for Login Button
        button1_title='Login'
        self.button1=Button(
                            self.my_container1,text=button1_title,font=('Veranda',20),
                            height='3',width='20',command=curry(self.decision_handling,'Login'))
        self.button1.place(relx='0.5',rely='0.5',anchor='c')

        #widget for register button
        button1_title='Register'
        self.button2=Button(
                            self.my_container1,text=button1_title,font=('Veranda',20),
                            height='3',width='20',command=curry(self.decision_handling,
                            'Register' )
                            )
        self.button2.place(relx='0.5',rely='0.7',anchor ='c')

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        self.master.geometry(self._geom)
        self._geom=geom
    #new window for the register window

    def entry_callback(self,event):
        self.expression=event.widget

    def btn_click(self,item):

        if self.expression is None:
            return
        if item=='Clear':
            self.expression.delete(0,END)
        elif item=='Bs':
            tempV = self.expression.get()
            tempV = tempV[0:-1]
            self.expression.delete(0,END)
            self.expression.insert(0,tempV)
        elif item=="Space":
            item=' '
            self.expression.insert(END,str(item))
        else:
            self.expression.insert(END,str(item))

        #callback for both register and login button
    def Log_Reg(self,window_name):
        self.username = StringVar()
        self.pass_date = StringVar()
        temp = False
        button = "Login"
        show = '*'
        callback = curry(self.database_id.Login,self.username)
        if window_name == 'Login':
            text1 = "UserID * "
            text2 = "Password * "
            temp = False
            button = "Login"
            y = 0.27
            show = '*'
            callback = curry(self.database_id.Login,self.username)
        else:
            text1 = "User Name * "
            text2 = "Date of Birth * "
            button = "Register"
            temp = True
            y = 0.25
            show = None
            callback = curry(self.database_id.Register, self.username,self.pass_date)
         # Set username label
        username_label = Label(self.register_screen, text=text1,font=self.label_font)
<<<<<<< HEAD
        username_label.place(relx=0.5,rely=0.08,anchor='c')
=======
        username_label.place(relx=0.5,rely=0.1,anchor='c')
>>>>>>> 46c6ccbaa747bef546d1d991583ef26dc12ee25c

    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
        username_entry = Entry(
                                self.register_screen,font=self.entry_font,
                                textvariable=self.username,
                            )
                            
        username_entry.bind('<Button-1>',self.entry_callback)
<<<<<<< HEAD
        username_entry.place(relx=0.5,rely=0.15,anchor='c')

         # Set password label
        password_label = Label(self.register_screen, text=text2,font=self.label_font)
        password_label.place(relx=0.5,rely=0.23,anchor='c')
=======
        username_entry.place(relx=0.5,rely=0.17,anchor='c')

         # Set password label
        password_label = Label(self.register_screen, text=text2,font=self.label_font)
        password_label.place(relx=0.5,rely=0.24,anchor='c')
>>>>>>> 46c6ccbaa747bef546d1d991583ef26dc12ee25c
        if temp == True:
             # Set password label
            password_label = Label(self.register_screen, text="Year/Month/day *",font=('Veranda',18))
            password_label.place(relx=0.5,rely=0.28,anchor='c')

    # Set password entry
        password = Entry(
                                    self.register_screen, textvariable=self.pass_date,
                                    show=show,font=self.entry_font,
                                    )
        password.place(relx=0.5,rely=0.35,anchor='c')
        password.bind('<Button-1>',self.entry_callback)

        # Set register button
        decide_button=Button(
<<<<<<< HEAD
                                self.register_screen,command=curry(self.diplay_output,2),font = self.button_font,
=======
<<<<<<< HEAD
                                self.register_screen,command=curry(self.diplay_output,0),font = self.button_font,
>>>>>>> 4d86658c9f73db8c882d22c6a6aa0140e580172c
                                text=button, width=10, height=3, bg="red",
                                    )
        decide_button.place(relx=0.85,rely=0.32,anchor='c')
        
    def BIA_GUI(self):
         
        
        render = ImageTk.PhotoImage(Image.open('GUIS/Selcouth_BIA.jpg'))
        canvas = Canvas(self.register_screen, width = self.register_screen.winfo_screenwidth(), height = self.register_screen.winfo_screenheight(), bg = "blue")  
        canvas.pack()
       
        canvas.create_image(0,0,anchor = NW, image=render)
        
        #Body weight
        canvas.create_text(232,106,fill="white",font="Times 28 italic bold",text=str(self.database_id.User_database["Weight"]))
        #Water Content
        canvas.create_text(788,106,fill="white",font="Times 28 italic bold",text=str(self.database_id.User_database["Water"]))
        #BMI
        canvas.create_text(131,220,fill="white",font="Times 28 italic bold",text="2.5")
        #Calorie
        canvas.create_text(890,220,fill="white",font="Times 25 italic bold",text=str(self.database_id.User_database["Calorie"]))
        #MuscleRate
        canvas.create_text(232,372,fill="white",font="Times 28 italic bold",text="60")
        #Body fat
        canvas.create_text(789,372,fill="white",font="Times 28 italic bold",text=str(self.database_id.User_database["Fat"]))
        #BoneMass
        canvas.create_text(131,480,fill="white",font="Times 28 italic bold",text=str(self.database_id.User_database["BoneMass"]))
        #Metabolic Age
        canvas.create_text(890,480,fill="white",font="Times 28 italic bold",text=str(self.database_id.User_database["MAge"]))
        
        canvas.image = render
        self.register_screen.update()  
        
        
    

    def Bloodpressure(self):
        
        render = ImageTk.PhotoImage(Image.open('GUIS/bp.jpg'))
        
       
        self.canvas.create_image(0,0,anchor = NW, image=render)
         #Systolic
        self.canvas.create_text(706,130,fill="white",font="Times 50 italic bold",text=str(self.database_id.User_database["Systolic"]))
       
        #Disatolic
        self.canvas.create_text(706,309,fill="white",font="Times 50 italic bold",text=str(self.database_id.User_database["Diastolic"]))
        #HeartBeat
        self.canvas.create_text(706,495,fill="white",font="Times 50 italic bold",text=str(self.database_id.User_database["HearBeat"]))
         

        self.canvas.image = render
    
        self.register_screen.update()  


    def temp(self):
        render = ImageTk.PhotoImage(Image.open('GUIS/Temp_Selcouth.jpg'))
<<<<<<< HEAD
       
        self.canvas.create_image(0,0,anchor = NW, image=render)
        self.canvas.create_text(217,172,fill="red",font="Times 40 italic bold",text=str(self.database_id.User_database["Temp"]))
=======
=======
                                self.register_screen,command=curry(self.diplay_output,1),font = self.button_font,
                                text=button, width=10, height=3, bg="red",
                                    )
        decide_button.place(relx=0.85,rely=0.35,anchor='c')
        
    def BIA_GUI(self):
        
        load = Image.open('GUIS/Selcouth_BIA.jpg')
        render = ImageTk.PhotoImage(load)
>>>>>>> 46c6ccbaa747bef546d1d991583ef26dc12ee25c
        canvas = Canvas(self.register_screen, width = self.register_screen.winfo_screenwidth(), height = self.register_screen.winfo_screenheight(), bg = "blue")  
        canvas.pack()
       
        canvas.create_image(0,0,anchor = NW, image=render)
<<<<<<< HEAD
        canvas.create_text(217,172,fill="red",font="Times 40 italic bold",text=str(self.database_id.User_database["Temp"]))
>>>>>>> 4d86658c9f73db8c882d22c6a6aa0140e580172c
        f = float("{0:.2f}".format(self.database_id.User_database["Temp"] * 1.8+ 32))
        
        self.canvas.create_text(235,358,fill="red",font="Times 40 italic bold",text=str(f))

        self.canvas.image = render
        self.register_screen.update()  
        

    def show_video(self):
        
        canvas = Canvas(self.register_screen, width = self.register_screen.winfo_screenwidth(), height = self.register_screen.winfo_screenheight(), bg = "blue")  
        canvas.pack()

        c = np.load("show.npy")
        
          
            
    
        
       
        
            
    def diplay_output(self, disp_num):
        toshow = None
        
        data = 0
        
        if disp_num == 0:
            self.Uart.write(str(disp_num))
            i=0
            self.canvas = Canvas(self.register_screen, width = self.register_screen.winfo_screenwidth(), height = self.register_screen.winfo_screenheight(), bg = "blue")  
            self.canvas.pack()
           
            while self.Uart.status == False:
                render = ImageTk.PhotoImage(self.images[i])
                self.canvas.create_image(0,0,anchor = NW, image=render)
                self.register_screen.update()
                time.sleep(0.5)
                i = i +1
                if i > 4:
                    i = 0
                print("BP"+str(i))
            
            print(self.Uart.data)
            
            for i in self.Uart.data:
                
                if i == 's':
                    self.database_id.User_database["Systolic"] = data
                    print("s"+str(data))
                    data = 0
                    
                elif i == 'd':
                    self.database_id.User_database["Diastolic"] = data
                    print("d"+str(data))
                    data = 0
                    
                elif i == 'h':
                    print("h"+str(data))
                    self.database_id.User_database["HearBeat"] = data
                    data = 0
                    
                else :
                    data = 10*data + int(i)
                    
                    
            self.Bloodpressure()
            self.Uart.status == False
                
        elif disp_num == 1:

=======

        #Body weight
        canvas.create_text(232,106,fill="white",font="Times 28 italic bold",text=str(self.database_id.User_database["Weight"]))
        #Water Content
        canvas.create_text(788,106,fill="white",font="Times 28 italic bold",text=str(self.database_id.User_database["Water"]))
        #BMI
        canvas.create_text(131,220,fill="white",font="Times 28 italic bold",text="2.5")
        #Calorie
        canvas.create_text(890,220,fill="white",font="Times 25 italic bold",text=str(self.database_id.User_database["Calorie"]))
        #MuscleRate
        canvas.create_text(232,372,fill="white",font="Times 28 italic bold",text="60")
        #Body fat
        canvas.create_text(789,372,fill="white",font="Times 28 italic bold",text=str(self.database_id.User_database["Fat"]))
        #BoneMass
        canvas.create_text(131,480,fill="white",font="Times 28 italic bold",text=str(self.database_id.User_database["BoneMass"]))
        #Metabolic Age
        canvas.create_text(890,480,fill="white",font="Times 28 italic bold",text=str(self.database_id.User_database["Mage"]))
       
        self.register_screen.mainloop()  
        
        
    

    def Bloodpressure(self):
        
        render = ImageTk.PhotoImage(Image.open('GUIS/Temp_Selcouth.jpg'))
         #Body fat
        text = Label(self.register_screen, text=self.User_database["Systolic"],font=('Veranda',18))
        text.place(relx=0.7666,rely=0.63,anchor='c')
        #Bone Mass
        text = Label(self.register_screen, text=self.User_database["Diastolic"],font=('Veranda',18))
        text.place(relx=0.122,rely=0.83,anchor='c')
        #Metabolic Age
        text = Label(self.register_screen, text=self.User_database["HearBeat"],font=('Veranda',18))
        text.place(relx=0.87,rely=0.83,anchor='c')

        self.canvas.create_image(0,0,anchor = NW, image=render)


    def diplay_output(self, disp_num):
        toshow = None
        #self.Uart.write(str(disp_num))
        data = []
        if disp_num == 0:
            #while self.status == False:
            print("waiting\n")
        
            #for i in self.Uart.data :
            #if i =='s':
                
            # else:
                  #  data = data + str()
                    
                     
    
            self.Bloodpressure()
            
            
        elif disp_num == 1:
>>>>>>> 46c6ccbaa747bef546d1d991583ef26dc12ee25c
            self.BIA.connect()
            self.BIA.manager.run()
            self.database_id.User_database.update(self.BIA.body_composition())
            
            self.BIA_GUI()
            
        elif disp_num == 2:
<<<<<<< HEAD
            self.Uart.write(str(disp_num))
            i=0
            self.canvas = Canvas(self.register_screen, width = self.register_screen.winfo_screenwidth(), height = self.register_screen.winfo_screenheight(), bg = "blue")  
            self.canvas.pack()
            while self.Uart.status == False:
                render = ImageTk.PhotoImage(self.images[i])
                self.canvas.create_image(0,0,anchor = NW, image=render)
                self.register_screen.update()
                i = i +1
                if i > 4:
                    i = 0
        
                
                print("Temperature")
                
            print(self.Uart.data)
            
            for i in self.Uart.data:   
                if i == 't':
                    self.database_id.User_database["Temp"] = (data / 1000)
                    print("s"+str(data/1000))
                    data = 0 
                else:
                    data = 10*data + int(i)
                    
            self.temp()
=======
            load = Image.open('GUIS/Temp_Selcouth.jpg')
>>>>>>> 46c6ccbaa747bef546d1d991583ef26dc12ee25c
            
        elif disp_num == 3:
            load = Image.open('GUIS/BP.jpg')
        
       
    
<<<<<<< HEAD
        #self.register_screen.bind('<Motion>', self.motion)
=======
        self.register_screen.bind('<Motion>', self.motion)
>>>>>>> 46c6ccbaa747bef546d1d991583ef26dc12ee25c
        self.register_screen.mainloop()  


        
    def motion(self, event):
        x, y = event.x, event.y
<<<<<<< HEAD
        print('{}, {}'.format(x, y))
=======
        print('{}, {}'.format(x/1024, y/600))
>>>>>>> 46c6ccbaa747bef546d1d991583ef26dc12ee25c




         
    def decision_handling(self,  window_name):
    
        window_name=window_name
        self.register_screen=Toplevel()
        ws = self.register_screen.winfo_screenwidth()
        hs = self.register_screen.winfo_screenheight()

        self.register_screen.title(window_name)
        self.register_screen.geometry('%dx%d'%(ws,hs))

        self.entry_font=('Veranda',25)
        self.label_font=('Veranda',20)
        self.button_font=('Veranda',20)
        

    #variables for the user input
        
    #Login
       
        self.Log_Reg(window_name)
    
   

    #keypad gui


        btns_frame = Frame(self.register_screen, width = 312, height = 272.5, bg = "grey")
        btns_frame.place(relx=0.02,rely=0.43)

        btn_list = ['Clear',
        'Q',  'W',  'E',  'R',  'T',
        'Y',  'U',  'I',  'O',  'P',
        'A','S','D','F','G','H','J',
        'K','L','Z','X','C','V','B',
        'N','M',
        '0',  '1',  '2',  '3',  '4',
        '5',  '6',  '7',  '8',  '9','Bs' ]
        # create and position all buttons with a for-loop
        # r, c used for row, column grid values
        r = 1
        c = 0
        n = 0
        # list(range()) needed for Python3
        btn = list(range(len(btn_list)))
        
        for label in btn_list:
            h=2
            w=4

            cmd = partial(self.btn_click,btn_list[btn_list.index(label)] )
            btn[n] = Button(btns_frame ,font=self.button_font,text=label,height=2, width=4,command= cmd)

            # position the button
            btn[n].grid(row=r, column=c)
            # increment button index
            n += 1
            # update row/column position
            c += 1
            if c > 9:
                c = 0
                r += 1


#event handling function for the register and the login button



# root=Tk()
# #input_text=StringVar()
# #user_name=StringVar()
# #pass_word=StringVar()
# device = Database()
# localhost = 27017
# database = "Medicare_report"
# collections = "collection2"
# device.initialize(localhost ,database, collections)
# display = My_App(root,device)
# root.mainloop()



