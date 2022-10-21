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

#Add deropdown for debug mode
menu = Menu (root)
item = Menu (menu)
item.add_command(label='Debug')
menu. add_cascade(label='Debug Menue', menu=item)
root.config (menu=menu)

#Sperates the canvase into diffrent coloms
root.columnconfigure(5, weight = 1)
root.rowconfigure(4, weight = 1)

#Create the verticle line seperator
tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=0, rowspan=10, sticky='ns', padx=5, pady=5)


#Logo Loading
logo = Image.open("PerceptualLogoTransparent.png")
logo = logo.resize((250, 280))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo




# Add the image in the canvas
logo_label.grid(column = 0, row = 0)


root.mainloop()