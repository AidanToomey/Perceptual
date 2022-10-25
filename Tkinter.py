#Setting up how to open application windows, video https://www.youtube.com/watch?v=l4WOgef0pDU
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
root = tk.Tk()

# Format Window Name and Size
root.title("Perceptual Software")
root.geometry('1920x1080')

#Sperates the canvase into diffrent coloms
root.columnconfigure(6, weight = 1)
root.rowconfigure(5, weight = 1)

#Add deropdown for debug mode
def DropdownMenue():
    menu = Menu (root)
    item = Menu (menu)
    item.add_command(label='Debug')
    menu. add_cascade(label='Debug Menu', menu=item)
    root.config (menu=menu)

#Create the verticle line seperator
tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=0, rowspan=10, sticky='ns', padx=5, pady=5)

def LoadLogo():
    logo = Image.open("PerceptualLogoTransparent.png")
    logo = logo.resize((250, 250))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image = logo)
    logo_label.image = logo
    logo_label.grid(column = 0, row = 0)


#Dashboard drop
def LoadDashboard():
    Dashboard = Image.open("Mercades Dashboard .jpeg")
    Dashboard = Dashboard.resize((1325,500 ))
    Dashboard = ImageTk.PhotoImage(Dashboard)
    Dashboard_label = tk.Label(image = Dashboard)
    Dashboard_label.image = Dashboard
    Dashboard_label.grid(column = 5, row = 4)


















DropdownMenue()
LoadLogo()
LoadDashboard()
root.mainloop()