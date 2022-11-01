import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import random

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
            self.menu = Menu (self.root)
            self.item = Menu (self.menu)
            self.item.add_command(label='Debug')
            self.menu. add_cascade(label='Debug Menu', menu=self.item)
            self.root.config (menu=self.menu)

        #Create the verticle/horizonatal line seperator
        tkinter.ttk.Separator(self.root, orient=VERTICAL).grid(column=1, row=0, rowspan=10, sticky='ns', padx=0, pady=0)
        tkinter.ttk.Separator(self.root, orient=HORIZONTAL).grid(column=1, row=1, columnspan=10, sticky='ew', padx=0, pady=0)

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


        def update_text(NameOfLabel, UpdatedValue):
            # Configuring the text in Label widget
            self.NameOfLabel.configure(text=UpdatedValue)

        DropdownMenue()
        LoadLogo()
        LoadDashboard()
        self.root.mainloop()

MyGUI()


##Other Teams code
NumOfStrikes = 0
while NumOfStrikes <= 3:
    if(random.randint(1,10) == 5):
        