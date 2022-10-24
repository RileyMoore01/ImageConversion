# import subprocess

from tkinter import *
from PIL import ImageTk, Image
from time import sleep
# from picamera import PiCamera 

###   Global Variables   ###
THRESHOLD = 0


###   Window   ###
win=Tk()
win.geometry("800x450")
win.config(bg='black')
win.wm_title("Pear Pi")


###   Functions   ###
def cal_sum():
    t1=int(a.get())
    if(t1>=0 | t1 < 0):
        print(t1)
    else:
        t1 = 0
        print(t1)
#    label.config(text=t1)

def clickRun():
    print("uncomment this code")
    # mainV2()

def clickCamOn():
    print("uncomment this code")
    # camera = PiCamera()
    # camera.start_preview()
    # sleep(20)
    # camera.stop_preview()

def clickRefImage():
    print("uncomment this code")
    # subprocess.call((['raspistill -o /home/pearpi/Desktop/Images/ref.jpg']),shell=True)

def sliderChanged(self, val):
    THRESHOLD = val
    displayThreshold = Label(self.master, text=f"{THRESHOLD}")
    displayThreshold.config(font =("Courier", 20))
    displayThreshold.place(x=10,y=80)

def clickExitButton():
    exit()




###    BUTTONS   ###
cameraOn = Button(win, text="On/Off", command=clickCamOn)
takeRefImage = Button(win, text="Ref", command=clickRefImage)
runProgram = Button(win, text="Run", command=clickRun)
exitButton = Button(win, text="Exit", command=clickExitButton)



###   Slider   ###
slider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=sliderChanged)
displayThreshold = Label(win, text=f"{THRESHOLD}")
displayThreshold.config(font =("Courier", 15))
display = Label(win, text="Detail")
thresRange = Label(win, text="(0-100)")



###   PLACEMENTS   ###
cameraOn.place(x=15,y=10)
takeRefImage.place(x=85, y=10)
runProgram.place(x=140,y=10)
exitButton.place(x=200, y=10)
slider.place(x=20, y=135)
displayThreshold.place(x=20,y=80)
display.place(x=60,y=80)



###   Labels   ###
Label(win, text="Time Delay", font=('Calibri 10')).pack()
a=Entry(win, width=35)
a.pack()
Button(win, text="Set", command=cal_sum).pack()

img = ImageTk.PhotoImage(Image.open("video.jpg"))  
l=Label(image=img)
l.pack()


win.mainloop()
