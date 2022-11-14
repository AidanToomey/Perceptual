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
<<<<<<< Updated upstream
=======
data = {'x': x,
         'y': y
         }
df2 = pd.DataFrame(data)

>>>>>>> Stashed changes

root = tk.Tk()
root.title("Perceptual Threading")
root.geometry("1650x600")

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
<<<<<<< Updated upstream
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
=======
    Dashboard_label.grid(column = 3, row = 0, columnspan=3, rowspan=2)

LoadLogo()
LoadDashboard()


figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().grid(column = 6,row = 0)
df2 = df2[['x', 'y']].groupby('x').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')
>>>>>>> Stashed changes

def RefreshGraph():
    # updating the value of x and y
    NewData = {'x': x,
         'y': y
         }
    dfN = pd.DataFrame(NewData)

    #Reprint Graph
    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().grid(column = 6,row = 0)
    dfN = dfN[['x', 'y']].groupby('x').sum()
    dfN.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Year Vs. Unemployment Rate')    

def MouseGraph():
    control = True
    count = 0
    t = 1
    inc = .1
    check1, check2, check3 = 0, 1, 2
    screenY = 540
    turns = 0

    mouse.moveTo(960, screenY)
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

def MouseGraph2():
    control = True
    count = 0
    t = 1
    inc = .1
    check1, check2, check3 = 0, 1, 2
    screenY = 540
    turns = 0

    mouse.moveTo(960, screenY)
    while control:
        pValues = mouse.position()
        x.append(inc * t)

        #Makes sure mouse is in the middle of the screen.
        if pValues[1] > 540 or pValues[1] < 540:
            mouse.moveTo(pValues[0], 540)

        if turns > -1: 
            y.append(int(pValues[0] / 5.333))

        if turns == -1: 
            y.append(int((pValues[0] - 1920) / 5.333))
        
        if pValues[0] <= 0 and turns > -1:
            mouse.moveTo(1919, screenY)
            turns -= 1
    
        if pValues[0] >= 1910 and turns < 0: 
            mouse.moveTo(10, screenY)
            turns += 1
    
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

        if count > 200:
            control = False
            break
        time.sleep(inc)

DebugNumber = Label(root, text="Debug Number!")
DebugNumber.grid(column= 0, row= 1)

StartBackendDebug = Button(root, text="Start Debug", command = threading.Thread(target=BackEndDebug).start)
StartBackendDebug.grid(column= 0, row= 2)

BlankSpace = Label(root, text="")
BlankSpace.grid(column= 0, row= 3)

StartGraph = Label(root, text="Data Collection")
StartGraph.grid(column= 0, row= 4)

StartGraphButton = Button(root, text="Begin", command = threading.Thread(target=MouseGraph2).start)
StartGraphButton.grid(column= 0, row= 5)
<<<<<<< Updated upstream
t1 = threading.Thread(target=RefreshGraph, args=[])
=======
>>>>>>> Stashed changes

BlankSpace = Label(root, text="")
BlankSpace.grid(column= 0, row= 6)

UpdateGraph = Label(root, text="Update Graph")
UpdateGraph.grid(column= 0, row= 7)

UpdateGraphButton = Button(root, text="Reset", command = threading.Thread(target=RefreshGraph).start)
UpdateGraphButton.grid(column= 0, row= 8)


root.mainloop()