import time

import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import random
import threading

#imports for BackEnd
import pyautogui as mouse
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


#Created Global Array
x = []
y = []

root = tk.Tk()
root.title("Perceptual Threading")
root.geometry("1600x600")

#Sperates the canvase into diffrent coloms
root.columnconfigure(6, weight = 0)
root.rowconfigure(10, weight = 0)

def BackEndDebug():
    DebugInt = 0
    while(DebugInt != -1):
        DebugNumber.config(text=f'Random Number: {DebugInt}')
        DebugInt += 1
        time.sleep(0.0000000001)

#Load Logo
def LoadLogo():
    logo = Image.open("PerceptualLogoTransparent.png")
    logo = logo.resize((125, 125))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image = logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=0)

#Load Dashboard
def LoadDashboard():
    Dashboard = Image.open("Mercades Dashboard .jpeg")
    Dashboard = Dashboard.resize((1000,400))
    Dashboard = ImageTk.PhotoImage(Dashboard)
    Dashboard_label = tk.Label(image = Dashboard)
    Dashboard_label.image = Dashboard
    Dashboard_label.grid(column = 6, row = 0, columnspan=3, rowspan=2)

#Load Plot
def LoadPlot():
    # enable interactive mode
    plt.ion()
 
    # creating subplot and figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot(x, y)
 
    # setting labels
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

def RefreshGraph():
    # updating the value of x and y
    line1.set_xdata(x*_)
    line1.set_ydata(y)
    
    # re-drawing the figure
    LoadPlot.plot1.canvas.draw()
     
    # to flush the GUI events
    LoadPlot.plot1.canvas.flush_events()
    time.sleep(0.1)    

def MouseGraph():
    control = True
    count = 0
    t = 1
    inc = .1
    check1, check2, check3 = 0, 1, 2

    mouse.moveTo(960, 540)
    while control:
        thing = mouse.position()
        y.append(thing[0] - 960)
        x.append(inc * t)
        if thing[1] > 540 or thing[1] < 540:
            mouse.moveTo(thing[0], 540)
        count += 1
        t += 1
        if count > 2:
            if (y[check2] < y[check1] and y[check2] < y[check3]) or (y[check2] == y[check1] and y[check2] < y[check3]):
                print(f'{y[check2]} is the relative minimum.')
            if (y[check2] > y[check1] and y[check2] > y[check3]) or (y[check2] == y[check1] and y[check2] > y[check3]):
                print(f'{y[check2]} is the relative maximum.')
            check1 += 1
            check2 += 1
            check3 += 1

        if count > 100:
            control = False
            break
        time.sleep(inc)


DebugNumber = Label(root, text="Debug Number!")
DebugNumber.grid(column= 0, row= 1)

StartBackendDebug = Button(root, text="Start the BackendDebug", command = threading.Thread(target=BackEndDebug).start)
StartBackendDebug.grid(column= 0, row= 2)

BlankSpace = Label(root, text="")
BlankSpace.grid(column= 0, row= 3)

StartGraph = Label(root, text="Data Collection")
StartGraph.grid(column= 0, row= 4)

StartGraphButton = Button(root, text="Begin", command = threading.Thread(target=MouseGraph).start)
StartGraphButton.grid(column= 0, row= 5)
t1 = threading.Thread(target=RefreshGraph, args=[])


LoadLogo()
LoadDashboard()
LoadPlot()

root.mainloop()