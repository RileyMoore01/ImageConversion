import subprocess

# from picamera import PiCamera
from time import sleep
from tkinter import *
from tkinter.ttk import *

###   Global Attributes   ###
REF = "ref.jpg"
THRESHOLD = 0
DISPLAY_THRES = Label()

def easteregg():
    print("hit the easter egg function");
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        # image = PhotoImage(file = r'camera.png')

        ###    BUTTONS   ###
        cameraOn = Button(self, text="On/Off", command=self.clickCamOn)
        takeRefImage = Button(self, text="Ref", command=self.clickRefImage)
        runProgram = Button(self, text="Run", command=self.clickRun)
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        # imageButton = Button(self, image = image, command = easteregg)

        ###   Labels   ###
        timeEntry = Entry(self)
        timeEntry.grid(row = 0, column=1)
        print(timeEntry.get())
        ###   Images   ###
        # img = PhotoImage(file='camera.png')
        # imgLabel = Label(image=img)
        # button = Button(master, image=img, command=print("hello"))

        ###   FEATURE   ###
        slider = Scale(master, from_=0, to=100, orient=HORIZONTAL, command=self.sliderChanged)
        DISPLAY_THRES = Label(master, text=f"{THRESHOLD}")
        DISPLAY_THRES.config(font =("Courier", 15))
        display = Label(master, text="Detail")
        thresRange = Label(master, text="(0-100)")

        ###   PLACEMENTS   ###
        cameraOn.place(x=10,y=10)
        takeRefImage.place(x=90, y=10)
        runProgram.place(x=170,y=10)
        exitButton.place(x=250, y=10)
        slider.place(x=20, y=135)
        DISPLAY_THRES.place(x=20,y=80)
        display.place(x=60,y=80)
        thresRange.place(x=60,y=110)
        # imageButton.grid(row = 18, column=7)
        # button.place(x=120, y=120)

    def clickRun(self):
        # mainV2()
        print('test')

    def clickCamOn(self):
        print("uncomment this code")
        # camera = PiCamera()
        # camera.start_preview()
        # sleep(20)
        # camera.stop_preview()

    def clickRefImage(self):
        # subprocess.call((['raspistill -o /home/pearpi/Desktop/Images/ref.jpg']),shell=True)
        print('ref image')

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
# root.configure(bg='black')
root.mainloop()