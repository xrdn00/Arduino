from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import time


root = Tk()

now = datetime.now()


root.title('Weather Report')
root.geometry("800x500")
#image file

images = [PhotoImage(file = "src/day1.gif"),PhotoImage(file = "src/night1.gif")]
bg = ImageTk.PhotoImage(file="src/day.gif")
bg1 = ImageTk.PhotoImage(file="src/night.gif")
#canvas
global count
count = -1

global h,m,s
h = ""
m = ""
s = ""

def clock():
    global h,m,s
    h = time.strftime("%H")
    m = time.strftime("%M")
    s = time.strftime("%S")
        
    
    label1.config(text =h+ ":" + m + ":" + s)
    label1.after(1000,clock)
    
canvas = Canvas(root,width = 800, height = 500,highlightthickness = 0)
label1 = Label(canvas, text = "", font=("Helvetica",20),fg = "green",bg = "lightblue")

label1.pack(pady=20)
clock()
canvas.pack(fill=BOTH, expand = True)
#image inside canvas

canvas.create_image(0,0, image = images[0], anchor = 'nw')

def next1():
    global h,m,s
    time_h = int(h)
    time_m = int(m)
    time_s = int(s)

    if time_s <= 30:
        canvas.create_image(0,0, image=images[0],anchor = 'nw')
    elif time_s >= 30:
        canvas.create_image(0,0, image=images[1],anchor = 'nw')
        
        
    root.after(1000,next1)
next1()
        

#icon
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)
#icon
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)


    

root.eval('tk::PlaceWindow . center')
root.resizable(width=False, height=False)
root.mainloop()


