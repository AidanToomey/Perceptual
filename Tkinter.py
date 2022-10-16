#Setting up how to open application windows, video https://www.youtube.com/watch?v=l4WOgef0pDU
import tkinter as tk
from PIL import Image, ImageTk


# Create an instance of tkinter frame or window
win = tk.Tk()



# Create a canvas widget
canvas = tk.Canvas(win, width=700, height=350)
#Sperates the canvase into diffrent coloms
canvas.grid(columnspan=5)



#Logo Loading
logo = Image.open("PerceptualLogoTransparent.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo



# Add the image in the canvas
logo_label.grid(column = 0, row = 0)


win.mainloop()