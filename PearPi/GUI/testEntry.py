from tkinter import *

win=Tk()

win.geometry("700x350")

def cal_sum():
   t1=int(a.get())
#    label.config(text=t1)

Label(win, text="Time Delay", font=('Calibri 10')).pack()
a=Entry(win, width=35)
a.pack()

Button(win, text="Set", command=cal_sum).pack()

win.mainloop()
