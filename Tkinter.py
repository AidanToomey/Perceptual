#Setting up how to open application windows, video https://www.youtube.com/watch?v=l4WOgef0pDU
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win = tk.Tk()

# Format Window Name and Size
win.title("Perceptual Software")
win. geometry('1920x1080')

#Sperates the canvase into diffrent coloms
win.columnconfigure(5, weight = 1)
win.rowconfigure(4, weight = 1)

#Create the verticle line seperator
tkinter.ttk.Separator(win, orient=VERTICAL).grid(column=1, row=0, rowspan=10, sticky='ns', padx=5, pady=5)


#Logo Loading
logo = Image.open("PerceptualLogoTransparent.png")
logo = logo.resize((250, 280))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo




# Add the image in the canvas
logo_label.grid(column = 0, row = 0)


win.mainloop()