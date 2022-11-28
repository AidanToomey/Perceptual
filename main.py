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

screenX, screenY = 1920, 1080
canvasX, canvasY = 1650, 600
bgColor = '#131418' 
bgOffset = '#91a1ad'
bgOrange = '#ec9b45'

x = []
y = []
data = {
    'x': x,
    'y': y
}
df2 = pd.DataFrame(data)
strikes = 0

#-----------> FUNCTIONS 
#Strike 1 and Strike 2 Made By Stone Nguyen 
def Strike1():
    Strike1 = ImageTk.PhotoImage(Image.open("Pictures/1st Strike Distracted driving.jpeg"))
    FrameStrike1 = frame(125, 125, 250, 300)
    Strike1_label = tk.Label(FrameStrike1, image=Strike1).pack()
    time.sleep(5)
    FrameStrike1.destroy()


def Strike2(): 
     Strike2 = ImageTk.PhotoImage(Image.open("Pictures/2nd Strike Distracted driving.jpeg"))
     FrameStrike2 = frame(125, 125, 250, 250)
     Strike2_label = tk.Label(FrameStrike2, image=Strike2).pack()
     time.sleep(5)
     FrameStrike2.destroy()

#RefreshGraph Made By Aidan Toomey, Helped by Stone Nguyen  
def RefreshGraph():
    # updating the value of x and y
    NewData = {
        'x': x,
        'y': y
    }
    dfN = pd.DataFrame(NewData)

    #Reprint Graph
    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, frame(1000, 400, 1350, 325)).get_tk_widget().pack(side='right')
    dfN = dfN[['x', 'y']].groupby('x').sum()
    dfN.plot(kind='line', legend=True, ax=ax2, color='r', marker='', fontsize=10)
    ax2.set_title('[POST] Wheel Angle * Time')
    ax2.set(xlabel='Time', ylabel='Rotation')  
#clamp Made By Jack Brewster 
def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)
#MouseGraph Mainly Made By Sean Bevensee and Jack Brewster, Helped by Stone Nguyen and Aidan Toomey
def MouseGraph(): 
    mouse.moveTo(10, 540)
    
    mouse_val_x = mouse.position()[0]
    mouse_val_change = 0 
    mouse_val_distance = 0

    wheel_val_deg = 0

    t = 1
    inc = 0.1
    check1, check2, check3 = 0, 1, 2
    relMax, relMin = False, False 
    Max, Min = 0, 0
    timesMax, timesMin = 0, 0
    strikes = 0

    time.sleep(3)
    while True:
        mouse_val_x = mouse.position()[0]

        if (mouse_val_x >= screenX - 2): mouse.moveTo(5, screenY / 2); mouse_val_x = 5
        elif (mouse_val_x <= 2): mouse.moveTo(1915, screenY / 2); mouse_val_x = 1915
        else: mouse_val_x = mouse.position()[0]

        time.sleep(0.01)

        mouse_val_change = mouse.position()[0] - mouse_val_x    
        mouse_val_distance = clamp((mouse_val_distance + mouse_val_change), -(screenX), screenX) 

        wheel_val_deg = mouse_val_distance / screenX * 360

        x.append(inc * t)
        y.append(wheel_val_deg)

        if t > 2:
            if (y[check2] < y[check1] and y[check2] < y[check3]) or (y[check2] == y[check1] and y[check2] < y[check3]):
                #print(f'({y[check2]}, {x[-1]}) is the relative minimum.')
                relMin = True
                Min = y[check2]
                timesMin = x[-1]
                formula = 1
            if (y[check2] > y[check1] and y[check2] > y[check3]) or (y[check2] == y[check1] and y[check2] > y[check3]):
                #print(f'({y[check2]}, {x[-1]}) is the relative maximum.')
                relMax = True
                Max = y[check2]
                timesMax = x[-1]
                formula = 0

            if Max > Min:
                y2, y1 = Max, Min
                x2, x1 = timesMax, timesMin
        
            else:
                y1, y2 = Max, min
                x1, x2 = timesMax, timesMin

            if relMax and relMin:
                print(abs((y2 - y1) / (x2 - x1)))

                if abs((y2 - y1) / (x2 - x1)) > 200:
            
                    strikes += 1
                    print(strikes)
                relMax, relMin = False, False
    
            check1 += 1
            check2 += 1
            check3 += 1
        t += 1

        if strikes == 1: 
            strikes += 1
            Strike1t = threading.Thread(target=Strike1)
            Strike1t.start()

        if strikes == 3:
           strikes += 1 
           Strike2t = threading.Thread(target=Strike2)
           Strike2t.start()


        if strikes > 5:
            control = False
            RefreshGraph()
            break

            
#----------> CREATE CANVAS
#GUI Primarly Made By Aidan Toomey and Sean Bevennsee, Helped By Stone Nguyen and Amy Prieto 
root.title("Perceptual PDM Testing")
root.geometry("{0}x{1}+100+200".format(canvasX, canvasY))
root['background'] = bgColor
root.resizable(0,0) 

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

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, frame(1000, 400, 1350, 325)).get_tk_widget().pack(side='right')
df2 = df2[['x', 'y']].groupby('x').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Wheel Angle * Time')

#----------
#Overall Everybody Chipped In Their Part and It Was Hard To Comment On Who Did What Because We All Helped Each Other On Everything. 

root.mainloop()
