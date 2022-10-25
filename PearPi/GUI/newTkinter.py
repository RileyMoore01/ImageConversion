# import subprocess

from tkinter import *
# from picamera import PiCamera
from time import sleep

###   Global Variables   ###
THRESHOLD = 0


###   Window   ###
win=Tk()
win.geometry("700x350")
win.config(bg='white')
win.wm_title("Pear Pi")



###   Functions   ###
def cal_sum():
    t1=int(a.get())
#    label.config(text=t1)

def clickRun(self):
    print("uncomment this code")
    # mainV2()

def clickCamOn(self):
    print("uncomment this code")
    # camera = PiCamera()
    # camera.start_preview()
    # sleep(20)
    # camera.stop_preview()

def clickRefImage(self):
    print("uncomment this code")
    # subprocess.call((['raspistill -o /home/pearpi/Desktop/Images/ref.jpg']),shell=True)

def sliderChanged(self, val):
    THRESHOLD = val
    DISPLAY_THRES = Label(self.master, text=f"{THRESHOLD}")
    DISPLAY_THRES.config(font =("Courier", 20))
    DISPLAY_THRES.place(x=10,y=80)

def my_command():
    text.config(text= "You have clicked Me...")

def clickExitButton(self):
    exit()




###    BUTTONS   ###
cameraOn = Button(win, text="On/Off", command=clickCamOn)
takeRefImage = Button(win, text="Ref", command=clickRefImage)
runProgram = Button(win, text="Run", command=clickRun)
exitButton = Button(win, text="Exit", command=clickExitButton)



###    IMAGE BUTTONS   ###
click_btn = PhotoImage(file='GUI/camera.gif')
click_btn = click_btn.subsample(2, 2)
cameraBtn_label = Label(image=click_btn)
cameraBtn_label.config(font=('Helvatical bold', 5))
button= Button(win, image=click_btn,command= my_command,borderwidth=0
    , height=65, width=65)
button.pack(pady=30)
text= Label(win, text= "")
text.pack(pady=30)



###   Slider   ###
slider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=sliderChanged)
DISPLAY_THRES = Label(win, text=f"{THRESHOLD}")
DISPLAY_THRES.config(font =("Courier", 15))
display = Label(win, text="Detail")
thresRange = Label(win, text="(0-100)")



###   PLACEMENTS   ###
cameraOn.place(x=15,y=10)
takeRefImage.place(x=85, y=10)
runProgram.place(x=140,y=10)
exitButton.place(x=200, y=10)
slider.place(x=30, y=275)
DISPLAY_THRES.place(x=20,y=80)
display.place(x=60,y=80)



###   Labels   ###
Label(win, text="Time Delay", font=('Calibri 10')).pack()
a=Entry(win, width=35)
a.pack()
Button(win, text="Set", command=cal_sum).pack()



win.mainloop()
