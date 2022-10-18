import subprocess

# from picamera import PiCamera
from time import sleep
from tkinter import *

###   Global Attributes   ###
REF = "ref.jpg"
THRESHOLD = 0
DISPLAY_THRES = Label()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        ###    BUTTONS   ###
        cameraOn = Button(self, text="On/Off", command=self.clickCamOn)
        takeRefImage = Button(self, text="Ref", command=self.clickRefImage)
        runProgram = Button(self, text="Run", command=self.clickRun)
        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        ###   FEATURE   ###
        slider = Scale(master, from_=0, to=100, orient=HORIZONTAL, command=self.sliderChanged)
        DISPLAY_THRES = Label(master, text=f"{THRESHOLD}")
        DISPLAY_THRES.config(font =("Courier", 15))
        display = Label(master, text="Detail")
        thresRange = Label(master, text="(0-100)")

        ###   PLACEMENTS   ###
        cameraOn.place(x=15,y=10)
        takeRefImage.place(x=85, y=10)
        runProgram.place(x=140,y=10)
        exitButton.place(x=200, y=10)
        slider.place(x=20, y=135)
        DISPLAY_THRES.place(x=20,y=80)
        display.place(x=60,y=80)
        thresRange.place(x=60,y=110)

    def clickRun(self):
        mainV2()

    def clickCamOn(self):
        print("uncomment this code")
        # camera = PiCamera()
        # camera.start_preview()
        # sleep(20)
        # camera.stop_preview()

    def clickRefImage(self):
        subprocess.call((['raspistill -o /home/pearpi/Desktop/Images/ref.jpg']),shell=True)

    def sliderChanged(self, val):
        THRESHOLD = val
        DISPLAY_THRES = Label(self.master, text=f"{THRESHOLD}")
        DISPLAY_THRES.config(font =("Courier", 20))
        DISPLAY_THRES.place(x=10,y=80)

    def clickExitButton(self):
        exit()
        
root = Tk()
app = Window(root)
root.wm_title("Pear Pi V.1")
root.geometry("320x200")
root.mainloop()
