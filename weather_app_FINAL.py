from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import time
import customtkinter

root = Tk()

now = datetime.now()
root.resizable(width=False, height=False)
root.eval('tk::PlaceWindow . center')
root.title('Weather Report')
root.geometry("800x500")
#image file

images = [PhotoImage(file = "src/day1.gif"),PhotoImage(file = "src/night1.gif")]

#canvas
global count
count = -1

global h,m,s
h = ""
m = ""
s = ""
def confirm_connection():
    pass
    
def connect():
    pass
    
    


    

def destroy_w():
    root.destroy()
def clock():
    
    global h,m,s
    h = time.strftime("%H")
    m = time.strftime("%M")
    s = time.strftime("%S")
        
    
    label1.configure(text =h+ ":" + m + ":" + s+"\nTEMP: 37°C")
    label1.after(1000,clock)
    
canvas = Canvas(root,width = 800, height = 500,highlightthickness = 0)
label1 = customtkinter.CTkButton(canvas, text = "",width = 100,height=50,corner_radius = 20,text_color = "gold",bg_color = "lightblue")
label1.pack(pady=20)
label2 = customtkinter.CTkLabel(canvas,text = "Humidity: ",text_color = "gold",bg_color = "black")
label2.pack(side = "left",anchor = "se",padx = 20)

label3 = customtkinter.CTkLabel(canvas,text = "HIGH",text_color = "red",bg_color = "black")
label3.pack(side = "left",anchor = "sw",padx = 10)
button1 = customtkinter.CTkButton(canvas, text = "Disconnect",width = 100,height=20,corner_radius = 10,text_color = "red",bg_color = "lightblue",fg_color = "white",command = destroy_w)
button1.pack(side = "right",anchor = "se",pady=10)

button2 = customtkinter.CTkButton(canvas, text = "Connect",width = 100,height=20,corner_radius = 10,text_color = "green",bg_color = "lightblue",fg_color = "white",command = connect)
button2.pack(side = "right",anchor = "se")
button2.place(x=700,y=440)

button3 = customtkinter.CTkButton(canvas, text = "Weather Device Status:",width = 100,height=20,corner_radius = 10,text_color = "green",bg_color = "lightblue",fg_color = "white")
button3.pack(side = "left",anchor = "nw",padx=0)
button3.place(x=10,y=440)
clock()
canvas.pack(fill=BOTH, expand = True)
#image inside canvas



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


    




root.mainloop()


