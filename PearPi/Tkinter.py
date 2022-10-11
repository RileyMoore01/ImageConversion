import subprocess

# from picamera import PiCamera
from time import sleep
from tkinter import *

###   Global Attributes   ###
REF = "ref.jpg"


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
        slider = Scale(master, from_=0, to=100, orient=HORIZONTAL)
        slider.pack()
        print(slider)

        ###   PLACEMENTS   ###
        cameraOn.place(x=10, y=5)
        takeRefImage.place(x=65,y=5)
        runProgram.place(x=275,y=140)
        exitButton.place(x=275, y=170)
        slider.place(x=10, y=150)

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

    def clickExitButton(self):
        exit()
        
root = Tk()
app = Window(root)
root.wm_title("Pear Pi V.1")
root.geometry("320x200")
root.mainloop()