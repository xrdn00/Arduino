from tkinter import *
from PIL import ImageTk, Image
#107frames

root = Tk()
root.title('Weather Report')
root.geometry("800x500")
#image file
bg = ImageTk.PhotoImage(file="src/day.gif")
#canvas
canvas = Canvas(root,width = 800, height = 500)
canvas.pack(fill=BOTH, expand = True)
#image inside canvas
canvas.create_image(0,0, image = bg, anchor = 'nw')
#resize window function
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("src/day.gif")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.LANCZOS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')
#icon
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)


root.bind("<Configure>", resize_image)

root.eval('tk::PlaceWindow . center')
root.mainloop()


