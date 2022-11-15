import random
import threading
import time
import tkinter as tk
from tkinter.ttk import *

import matplotlib.pyplot as plt
import pandas as pd
#imports for BackEnd
import pyautogui as mouse
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
from PIL import Image, ImageTk

#Created Global Array
x = []
y = []
data = {'x': x,
         'y': y
         }
df2 = pd.DataFrame(data)


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
    Dashboard_label.grid(column = 3, row = 0, columnspan=3, rowspan=2)

LoadLogo()
LoadDashboard()


figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().grid(column = 6, row = 0)
df2 = df2[['x', 'y']].groupby('x').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='b', marker='', fontsize=10)
ax2.set_title('Blank Graph')
ax2.set(xlabel='Time', ylabel='y-axis label')

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
    dfN.plot(kind='line', legend=True, ax=ax2, color='b', marker='', fontsize=10)
    ax2.set_title('Blank Graph')    
    

def MouseGraph2():
    control = True
    control = True

    strikes = 0
    t = 1
    inc = .5
    check1, check2, check3 = 0, 1, 2
    screenY = 540
    turns = 0
    relMax = False
    Max = 0
    relMin = False
    Min = 0
    safetyPer = 1
    timesMax = 0
    timesMin = 0
    formula = None

    mouse.moveTo(1, screenY)
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
            mouse.moveTo(1, screenY)
            turns += 1
    

        if t > 2:
            if (y[check2] < y[check1] and y[check2] < y[check3]) or (y[check2] == y[check1] and y[check2] < y[check3]):
                print(f'({y[check2]}, {x[-1]}) is the relative minimum.')
                relMin = True
                Min = y[check2]
                timesMin = x[-1]
                formula = 1
            if (y[check2] > y[check1] and y[check2] > y[check3]) or (y[check2] == y[check1] and y[check2] > y[check3]):
                print(f'({y[check2]}, {x[-1]}) is the relative maximum.')
                relMax = True
                Max = y[check2]
                timesMax = x[-1]
                formula = 0

            if relMax and relMin:
                if formula == 0:
                    print(abs((abs(Max) - abs(Min)) / abs(timesMax) - abs(timesMin)))
                    print("using increasing formula")
                    if abs((abs(Max) - abs(Min) / abs(timesMax) - abs(timesMin))) < 30:
                        strikes += 1
                        print(strikes)
                else:
                    print(abs((abs(Min) - abs(Max)) / abs(timesMin) - abs(timesMax)))
                    print("using decreasing slope formula")
                    if abs((abs(Min) - abs(Max) / abs(timesMin) - abs(timesMax))) < 30:
                        strikes += 1
                        print(strikes)

                relMax = False
                relMin = False
    
            check1 += 1
            check2 += 1
            check3 += 1
    
        t += 1

        if strikes > 2:
            control = False
            RefreshGraph()
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

BlankSpace = Label(root, text="")
BlankSpace.grid(column= 0, row= 6)


root.mainloop()