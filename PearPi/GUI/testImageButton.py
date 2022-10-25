from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.title("Test Image Button")
win.geometry("700x300")

def my_command():
   text.config(text= "You have clicked Me...")

# tempImg1 = Image.open('GUI/camera.gif')
# tempImg2 = tempImg1.resize((100, 50), Image.ANTIALIAS)
# img = PhotoImage(tempImg2)
# picture = Label(win, image=tempImg2)
# picture.grid(column=1, row=1)
temp = PhotoImage(file='GUI/camera.gif')
click_btn = temp.subsample(2, 2)



img_label= Label(image=click_btn)
img_label.config(font=('Helvatical bold',5))

button= Button(win, image=click_btn,command= my_command,borderwidth=0
   , height=150, width=150)
button.pack(pady=30)

text= Label(win, text= "")
text.pack(pady=30)



win.mainloop()
