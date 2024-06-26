from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import time
import customtkinter
import serial
import threading
root = Tk()
global serial_hum,serial_temp,serial_faren,light_dark

ser = serial.Serial('COM3',9600)


now = datetime.now()
root.resizable(width=False, height=False)
root.eval('tk::PlaceWindow . center')
root.title('Weather Report')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
app_width = 800
app_height = 500
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
root.geometry("{}x{}+{}+{}".format(app_width,app_height,int(x),int(y)))
#image file

images = [PhotoImage(file = "src/day1.gif"),PhotoImage(file = "src/night1.gif"),PhotoImage(file = "src/dim.gif")]

#canvas



global h,m,s
h = ""
m = ""
s = ""
def confirm_connection():
    pass

    
def connect():
    
    
    
    label0 = customtkinter.CTkLabel(canvas,text = "Connecting...      ",text_color = "black")
    label0.place(x=10,y=40)
    def destroy():
        label0.destroy()
    root.after(1000,destroy)
    def connected():
        root.after(1000)
    
        labelc = customtkinter.CTkLabel(canvas,text = "Connected",text_color = "green")
        labelc.place(x=10,y=40)
        root.after(1000,)
        def destroy_c():
            labelc.destroy()
        root.after(1000,destroy_c)
        
        
    root.after(1000,connected)
    
    
    
    
    
    


    

def disconnect():
    
    
    
    label0 = customtkinter.CTkLabel(canvas,text = "Disconnecting...",text_color = "black")
    label0.place(x=10,y=40)
    def destroy():
        label0.destroy()
    root.after(1000,destroy)
    def dconnected():
        root.after(1000)
    
        labelc = customtkinter.CTkLabel(canvas,text = "Disconnected",text_color = "red")
        labelc.place(x=10,y=40)
        def destroy_c():
            labelc.destroy()
        root.after(1000,destroy_c)
        
        
    root.after(1000,dconnected)
    
  
    
    
def clock():
    
    
    global h,m,s
    h = time.strftime("%H")
    m = time.strftime("%M")
    s = time.strftime("%S")

    
    
        
    
    button0.configure(text ="TIME:\n"+h+ ":" + m + ":" + s)
    root.after(100,clock)

    



def ld():
    
    b = ser.readline()
    edit1 = b.decode('utf-8')
    edit2 = edit1.replace('\n','')
    edit3 = edit2.replace('%','')
    serial_hum,serial_temp,serial_faren,light_dark = edit3.split(' ')
    
    
    
    
    if int(light_dark) <=290:
        label5.configure(text ="{} Too Bright".format(light_dark),text_color = 'red',bg_color = 'black')
        canvas.create_image(0,0, image=images[0],anchor = 'nw')
    elif int(light_dark) <=490:
        label5.configure(text ="{} Bright".format(light_dark),text_color = 'orange',bg_color = 'black')
        canvas.create_image(0,0, image=images[0],anchor = 'nw')
    elif int(light_dark) <=550:
        label5.configure(text ="{} Dim".format(light_dark),text_color = 'green',bg_color = 'black')
        canvas.create_image(0,0, image=images[2],anchor = 'nw')
    elif int(light_dark) <=690:
        label5.configure(text ="{} Dark".format(light_dark),text_color = 'violet',bg_color = 'black')
        canvas.create_image(0,0, image=images[1],anchor = 'nw')
    
        
    
    root.after(1000,ld)
        
    

def humidity():
    b = ser.readline()
    edit1 = b.decode('utf-8')
    edit2 = edit1.replace('\n','')
    edit3 = edit2.replace('%','')
    serial_hum,serial_temp,serial_faren,light_dark = edit3.split(' ')
    hum_convert = float(serial_hum)
    hum_perc = int(hum_convert)

    if float(serial_hum) <=30:
        label3.configure(text = "{}% LOW".format(hum_perc),text_color = 'red',bg_color = 'black')
    elif float(serial_hum) <=45:
        label3.configure(text = "{}% MEDIUM".format(hum_perc),text_color = 'orange',bg_color = 'black')
    elif float(serial_hum) <=60:
        label3.configure(text = "{}% HIGH".format(hum_perc),text_color = 'red',bg_color = 'black')
    elif float(serial_hum) >=60:
        label3.configure(text = "{}% DANGER".format(hum_perc),text_color = 'red',bg_color = 'black')
    else:
        label3.configure(text = "{}% ERROR".format(hum_perc),text_color = 'red',bg_color = 'black')
    root.after(200,humidity)

def temperature():
    b = ser.readline()
    edit1 = b.decode('utf-8')
    edit2 = edit1.replace('\n','')
    edit3 = edit2.replace('%','')
    serial_hum,serial_temp,serial_faren,light_dark = edit3.split(' ')
    a = float(serial_temp)
    b = int(a)
    f = ((b*5/9)+32)
    
    if b <= 25:
        label6.configure(text = "{}°C ~ {:.2f}°F COLD".format(a,f))
    elif b <= 30:
        label6.configure(text = "{}°C ~ {:.2f}°F COMFORTABLE".format(a,f))
    elif b <= 35:
        label6.configure(text = "{}°C ~ {:.2f}°F WARM".format(a,f))
    elif b <= 40:
        label6.configure(text = "{}°C ~ {:.2f}°F HOT".format(a,f))
    else:
        label6.configure(text = "ERROR")
    
    
    
    root.after(300,temperature)


        
    

        
    
    
    
#CANVAS    
canvas = Canvas(root,width = 800, height = 500,highlightthickness = 0)

button0 = customtkinter.CTkButton(canvas, text = "",width = 100,height=50,corner_radius = 20,text_color = "gold",bg_color = "lightblue")
button0.pack(pady=20)
button0.place(x=350,y=440)
label2 = customtkinter.CTkLabel(canvas,text = "Humidity: ",text_color = "gold",bg_color = "black")
label2.pack(side = "left",anchor = "se",padx = 20)

label3 = customtkinter.CTkLabel(canvas,text = "HIGH",text_color = "red",bg_color = "black")
label3.pack(side = "left",anchor = "sw",padx = 10)
button1 = customtkinter.CTkButton(canvas, text = "Disconnect",width = 90,height=20,corner_radius = 10,text_color = "red",bg_color = "lightblue",fg_color = "white",command = disconnect)
button1.pack(side = "right",anchor = "se",pady=10)
button1.place(x=700,y=470)

label4 = customtkinter.CTkLabel(canvas,text = "Light intensity:",text_color = "green",bg_color = "white")
label4.place(x=10,y=10)
label5 = customtkinter.CTkLabel(canvas,text = "LOW",text_color = "green",bg_color = "white")
label5.place(x=120,y=10)


button2 = customtkinter.CTkButton(canvas, text = "Connect",width = 90,height=20,corner_radius = 10,text_color = "green",bg_color = "lightblue",fg_color = "white",command = connect)
button2.pack(side = "right",anchor = "se",pady = 10)
button2.place(x=700,y=440)

label6 = customtkinter.CTkLabel(canvas, text = "",width = 100,height=20,corner_radius = 10,text_color = "green",bg_color = "lightblue",fg_color = "white")
label6.pack(side = "left",anchor = "nw",padx=0)
label6.place(x=20,y=440)

clock()
ld()
humidity()
temperature()


y = threading.Thread(target=ld)
y.start()

canvas.pack(fill=BOTH, expand = True)



#image changes when specific time conditions meet(NOT USED)
def next1():
    
    global h,m,s
    time_h = int(h)
    time_m = int(m)
    time_s = int(s)

    if time_h <= 6:
        canvas.create_image(0,0, image=images[1],anchor = 'nw')
    elif time_h <= 18:
        canvas.create_image(0,0, image=images[0],anchor = 'nw')
    elif time_h >=18:
        canvas.create_image(0,0, image=images[1],anchor = 'nw')
        
        
    root.after(1000,next1)
#next1()
        

#icon
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)



    




root.mainloop()


