import tkinter as tk
#import tkinter as tkk
from tkinter.ttk import *
from PIL import Image, ImageTk
import random
import threading

class MyGUI:

    def __init__(self):
        # Create an instance of tkinter frame or window
        self.root = tk.Tk()

        # Format Window Name and Size
        self.root.title("Perceptual Software")
        self.root.geometry('1920x1080')

        #Sperates the canvase into diffrent coloms
        self.root.columnconfigure(6, weight = 1)
        self.root.rowconfigure(6, weight = 1)

        #Add deropdown for debug mode
        def DropdownMenue():
            self.menu = tk.Menu (self.root)
            self.item = tk.Menu (self.menu)
            self.item.add_command(label='Debug')
            self.menu. add_cascade(label='Debug Menu', menu=self.item)
            self.root.config (menu=self.menu)

        #Create the verticle/horizonatal line seperator
        Separator(self.root, orient=tk.VERTICAL).grid(column=1, row=0, rowspan=10, sticky='ns', padx=0, pady=0)
        Separator(self.root, orient=tk.HORIZONTAL).grid(column=1, row=1, columnspan=10, sticky='ew', padx=0, pady=0)

        def LoadLogo():
            self.logo = Image.open("PerceptualLogoTransparent.png")
            self.logo = self.logo.resize((250, 250))
            self.logo = ImageTk.PhotoImage(self.logo)
            self.logo_label = tk.Label(image = self.logo)
            self.logo_label.image = self.logo
            self.logo_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)


        #Dashboard drop
        def LoadDashboard():
            self.Dashboard = Image.open("Mercades Dashboard .jpeg")
            self.Dashboard = self.Dashboard.resize((1550,600))
            self.Dashboard = ImageTk.PhotoImage(self.Dashboard)
            self.Dashboard_label = tk.Label(image = self.Dashboard)
            self.Dashboard_label.image = self.Dashboard
            self.Dashboard_label.grid(column = 2, row = 4, columnspan=6, rowspan=2)

        def Load1stStrike():
            self.Strike1 = Image.open("1st Strike Distracted driving.jpeg")
            self.Strike1 = self.Strike1.resize((250, 250))
            self.Strike1 = ImageTk.PhotoImage(self.Strike1)
            self.Strike1 = tk.Label(image = self.Strike1)
            self.Strike1.image = self.Strike1
            self.Strike1.grid(column=4, row=4)    

        def update_text(NameOfLabel, UpdatedValue):
            # Configuring the text in Label widget
            self.NameOfLabel.configure(text=UpdatedValue)

        #Debuging Values
        RandomNumber = Label(root, text="Not Working!")
        RandomNumber.grid(column = 2, row = 6)

        def DebuggingValue():
            DebugInt = 0
            while(DebugInt < 100):
                RandomNumber.config(text=f'Random Number: {random.randint(1,100)}')
                DebugInt += 1
                time.sleep(1)

        DropdownMenue()
        LoadLogo()
        LoadDashboard()
        self.root.mainloop()



def run_thread():
    db = threading.Thread(target = MyGUI.DebuggingValue())
    db.start()
    db.join()
    db = threading.Thread(target = MyGUI)
    db.start()
    db.join()

run_thread()


   