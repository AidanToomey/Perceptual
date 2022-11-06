import time
import tkinter as tk
#import tkinter as tkk
from tkinter.ttk import *
from PIL import Image, ImageTk
import random
import threading

root = tk.Tk()
root.title("Perceptual Threading")
root.geometry("800x400")

def BackEnd():
    DebugInt = 0
    while(DebugInt < 100):
        RandomNumber.config(text=f'Random Number: {random.randint(1,100)}')
        DebugInt += 1
        time.sleep(0.2)

def FrontEnd():
    DebugInt = 0
    while(DebugInt < 100):
        RandomNumber2.config(text=f'Random Number: {random.randint(1,100)}')
        DebugInt += 1
        time.sleep(0.2)

#Load Logo
def LoadLogo():
    logo = Image.open("PerceptualLogoTransparent.png")
    logo = logo.resize((250, 250))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image = logo)
    logo_label.image = logo
    logo_label.pack(padx=5, pady=20, side=tk.LEFT)

RandomNumber = Label(root, text="Hello There!")
RandomNumber.pack(pady=20)

RandomNumber2 = Label(root, text="Hello There!")
RandomNumber2.pack(pady=20)

StartBackend = Button(root, text="Start the Backend", command = threading.Thread(target=BackEnd).start)
StartBackend.pack(pady=20)

StartFrontend = Button(root, text="Start the Frontend", command = threading.Thread(target=FrontEnd).start)
StartFrontend.pack(pady=20)

LoadLogo()

root.mainloop()