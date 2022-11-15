import tkinter as tk
from PIL import ImageTk
from PIL import Image
import pyautogui 

# Sean - 11/15/2022, 1:24am; 
# this is the basic shit im using with the GlovePIE 
# script, just as proof that it works. 


class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=1000, height=1000)
        self.canvas.pack()

        self.update = self.draw().__next__
        master.after(100, self.update)

    def draw(self):
        image = Image.open(self.filename)
        angle = 0
        while True:
            tkimage = ImageTk.PhotoImage(image.rotate(-1 * pyautogui.position()[0] / 1920 * 360))
            canvas_obj = self.canvas.create_image(500, 500, image=tkimage)
            self.master.after_idle(self.update)
            yield 
            self.canvas.delete(canvas_obj)

root = tk.Tk()
app = SimpleApp(root, 'sWheel.png')
root.mainloop()