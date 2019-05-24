import tkinter as tk
from tkinter import *
from functools import partial
from database import Database



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
    def __init__(self,master,database_id):
        self.expression=None
        self.master=master #instance of the Tk library
        pad=3
        self.database_id = database_id
        self._geom='400x200+0+0'
        self.master.geometry("{0}x{1}+0+0".format(
            self.master.winfo_screenwidth()-pad, self.master.winfo_screenheight()-pad))
        self.master.bind('<Escape>',self.toggle_geom)
        self.master.title("Selcouth Health")

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
                            self.my_container1,text=button1_title,
                            height='2',width='30',command=curry(self.decision_handling,'Login'))
        self.button1.place(relx='0.5',rely='0.5',anchor='c')

        #widget for register button
        button1_title='Register'
        self.button2=Button(
                            self.my_container1,text=button1_title,
                            height='2',width='30',command=curry(self.decision_handling,
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
        else:
            self.expression.insert(END,str(item))

        #callback for both register and login button
    def decision_handling(self,  window_name):
        window_width=400
        window_height=150
    
        window_name=window_name
        register_screen=Toplevel()
        register_screen.title(window_name)
        register_screen.geometry('800x400')

                #creating the input frame
        """     input_frame = Frame(
                            register_screen, width = window_width,
                            height = window_height, bd = 0, highlightbackground = "black",
                            highlightcolor = "black", highlightthickness = 1,
                            )
        input_frame.pack(side = TOP)
        """

    #variables for the user input
        self.username = StringVar()
        self.password = StringVar()

    # Set label for user's instruction
        detail_label1=Label(register_screen,
                            text="Please enter details below",
                            bg="cyan",
                            )
        detail_label1.place(relx=0.5,rely=0.05,anchor='c')

    # Set username label
        username_label = Label(register_screen, text="Username * ")
        username_label.place(relx=0.5,rely=0.15,anchor='c')



    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
        username_entry = Entry(
                                register_screen,
                                textvariable=self.username,
                            )
        username_entry.bind('<Button-1>',self.entry_callback)
        username_entry.place(relx=0.5,rely=0.2,anchor='c')
    





    # Set password label
        password_label = Label(register_screen, text="Password * ")
        password_label.place(relx=0.5,rely=0.25,anchor='c')

    # Set password entry
        password_entry = Entry(
                                    register_screen, textvariable=self.password,
                                    show='*',
                                    )
        password_entry.place(relx=0.5,rely=0.3,anchor='c')
        password_entry.bind('<Button-1>',self.entry_callback)

        # Set register button
        decide_button=Button(
                                register_screen,command=curry(self.database_id.Login,3),
                                text=window_name, width=10, height=1, bg="red",
                                    )
        decide_button.place(relx=0.85,rely=0.35,anchor='c')

    #keypad gui


        btns_frame = Frame(register_screen, width = 312, height = 272.5, bg = "grey")
        btns_frame.place(relx=0.14,rely=0.4)

        btn_list = ['Clear',
        'A',  'B',  'C',  'D',  'E',
        'F',  'G',  'H',  'I',  'J',
        'K','L','M','N','O','P','Q',
        'R','S','T','U','V','W','X',
        'Y','Z',
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


            cmd = partial(self.btn_click,btn_list[btn_list.index(label)] )
            btn[n] = Button(btns_frame ,text=label,height=3, width=6,command= cmd)

            # position the button
            btn[n].grid(row=r, column=c)
            # increment button index
            n += 1
            # update row/column position
            c += 1
            if c > 7:
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



