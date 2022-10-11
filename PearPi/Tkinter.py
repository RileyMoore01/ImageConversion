import subprocess

from picamera import PiCamera
from time import sleep
from tkinter import *

###   Global Attributes   ###
REF = "ref.jpg"


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        cameraOn = Button(self, text="On/Off", command=self.clickCamOn)
        takeRefImage = Button(self, text="Ref", command=self.clickRefImage)
        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        takeRefImage.place(x=50,y=50)
        exitButton.place(x=0, y=0)

    def clickCamOn(self):
        camera = PiCamera()
        camera.start_preview()
        sleep(10)
        camera.stop_preview()

    def clickRefImage(self):
        subprocess.call((['raspistill -o /home/pearpi/Desktop/Images/ref.jpg']),shell=True)

    def clickExitButton(self):
        exit()
        
root = Tk()
app = Window(root)
root.wm_title("Pear Pi V.1")
root.geometry("320x200")
root.mainloop()