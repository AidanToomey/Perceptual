#----------> IMPORTS 
import time

import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import random
import threading

import pyautogui as mouse
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd

#----------> VARIABLES 
root = tk.Tk()

canvasX, canvasY = 1650, 600
bgColor = '#131418' 
bgOffset = '#91a1ad'
bgOrange = '#ec9b45'

x = []
y = []
data = {'x': x,
         'y': y
         }
df2 = pd.DataFrame(data)
strikes = 0

#----------->
# GRAPH FUNCTIONS GO HERE 

# figure2 = plt.Figure(figsize=(5, 4), dpi=100)
# ax2 = figure2.add_subplot(111)
# line2 = FigureCanvasTkAgg(figure2, root)
# line2.get_tk_widget().pack(side='right')
# df2 = df2[['x', 'y']].groupby('x').sum()
# df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
# ax2.set_title('Blank Graph')
# ax2.set(xlabel='Time', ylabel='y-axis label')

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
    line2.get_tk_widget().pack(side='right')
    dfN = dfN[['x', 'y']].groupby('x').sum()
    dfN.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Wheel Rotation')
    ax2.set(xlabel='Time', ylabel='Rotation')  

def MouseGraph():
    control = True
    strikes = 0
    t = 1
    inc = .1
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

            if Max > Min:
                y2 = Max
                y1 = Min
                x2 = timesMax
                x1 = timesMin
        
            else:
                y1 = Max
                y2 = Min
                x1 = timesMax
                x2 = timesMin

            if relMax and relMin:
                if abs((y2 - y1) / (x2 - x1)) > 300:
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
            break
        time.sleep(inc)



#----------> CREATE CANVAS
root.title("Perceptual PDM Testing")
root.geometry("{0}x{1}+100+200".format(canvasX, canvasY))
root['background'] = bgColor
root.resizable(0,0) 

#---Frame Function 
def frame(widthIn, heightIn, xIn, yIn): 
    frame = tk.Frame(root, width=widthIn, height=heightIn)#
    frame.pack()
    frame.place(anchor='center', x=xIn, y=yIn)

    return frame 

#---Screen Elements
logo = ImageTk.PhotoImage(Image.open("Pictures/PerceptualLogoTransparent.png").resize((150, 100))) 
logo_label = tk.Label(frame(150, 150, 100, 55), image=logo, bg="{0}".format(bgColor)).pack()
Dashboard = ImageTk.PhotoImage(Image.open("Pictures/Mercades Dashboard .jpeg").resize((1000,400)))
Dashboard_label = tk.Label(frame(1000, 400, 550, 325), image=Dashboard, bg="{0}".format(bgColor)).pack()

tk.Label(frame(50, 50, 275, 35), bg="{0}".format(bgColor), fg="white", text="PDM™ - Perceptual Driving Module").pack()
tk.Label(frame(50, 50, 435, 35), bg="{0}".format(bgColor), fg="{0}".format(bgOffset), text="VERSION 2.0.1:11.16.22").pack()

qButton = tk.Button(frame(10, 10, 330, 65), bg="{0}".format(bgOffset), font="System", command=root.quit, text="EXIT").pack()
gButton = tk.Button(frame(10, 10, 240, 65), bg="{0}".format(bgOrange), font="System", command = threading.Thread(target=MouseGraph).start, text="BEGIN TESTING").pack()
#threading.Thread(target=MouseGraph2).start command for ^ 

#----------



root.mainloop()
