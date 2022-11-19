import subprocess
import sys
# import easygui
# import wiringpi

from tkinter import *
from time import sleep
from time import sleep
# from matplotlib.pyplot import imread
from PIL import Image, ImageChops, ImageOps
from gpiozero import LightSensor, Buzzer
# from scipy.linalg import norm
from numpy import sum, average
from picamera import PiCamera

############################################################
##                      Global Variables                  ##
############################################################
THRESHOLD = 0
TIMEDELAY = 0
NEWTIMEDELAY = 0
BUTTON_HEIGHT = 150
BUTTON_WIDTH = 150
INDEX = 0


############################################################
##                      Main                              ##
############################################################



def CompareImages():
    global INDEX, THRESHOLD
    INDEX = 0
    thres = THRESHOLD % 10

    img1 = Image.open("Images/ref.jpg")
    img2 = Image.open("Images/pic"+str(INDEX)+".jpg")
    img2 = img2.resize(img1.size)

    #Grayscale
    img1 = img1.convert('L')
    img2 = img2.convert('L')

    #Threshold
    img1 = img1.point(lambda p: 255 if p > thres else 0)
    img2 = img2.point(lambda p: 255 if p > thres else 0)

    #Monochrome
    img1 = img1.convert('1')
    img2 = img2.convert('1')

    diff = ImageChops.difference(img1, img2)

    if diff.getbbox():
        # buzzer.on()
        sleep(1)
        # buzzer.off()
        diff.show()
        #16x20



def captureImage():
    global INDEX
    subprocess.call((['raspistill -o /home/pearpi/Desktop/Images/pic'+str(INDEX)+'.jpg']),shell=True)


def main():
    global TIMEDELAY
    # buzzer = Buzzer(17)

    # Read in the sensors output
    sensor = False;
    if(sensor):
        sleep(TIMEDELAY)
        captureImage()
        CompareImages()


############################################################
##                      Window                            ##
############################################################
win=Tk()
win.geometry("1050x535")
win.config(bg='white')
win.wm_title("Pear Pi")


############################################################
##                      Functions                         ##
############################################################
def RunProgram():
    print("*** Running program ***")
    main()

def PositionCamera():
    print("*** Turning on the camera ***")
    camera = PiCamera()
    camera.start_preview()
    sleep(10)
    camera.stop_preview()

def TakeReferenceImage():
    print("*** Taking reference Image ***")
    subprocess.call((['raspistill -o /home/pearpi/Desktop/Images/ref.jpg']),shell=True)

def Slider(val):
    global THRESHOLD
    THRESHOLD = val
    displayThreshold.config(text=f'{THRESHOLD}')

def TimeDelayAdd():
    global TIMEDELAY
    TIMEDELAY = TIMEDELAY + 1
    timeDelayDisplay.config(text=f'{TIMEDELAY}')

def TimeDelaySub():
    global TIMEDELAY
    TIMEDELAY = TIMEDELAY - 1
    timeDelayDisplay.config(text=f'{TIMEDELAY}')

def clickExitButton():
    exit()


############################################################
##                      Image Buttons                     ##
############################################################

# Position button  ---------------------------------------------------------------------
positionIcon = PhotoImage(file='/home/pearpi/Desktop/position.gif')
positionIcon = positionIcon.subsample(2, 2)

positionLabel = Label(image=positionIcon)
positionLabel.config(font=('Helvatical bold', 10), bg='white')

positionButton= Button(win, image=positionIcon,command= PositionCamera,borderwidth=0, highlightthickness=0
    , height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg='white')
positionButton.pack(pady=0, side=LEFT, anchor=N)


# Reference Image Button  ---------------------------------------------------------------
referenceIcon = PhotoImage(file='/home/pearpi/Desktop/camera.gif')
referenceIcon = referenceIcon.subsample(2, 2)

referenceLabel = Label(image=referenceIcon)
referenceLabel.config(font=('Helvatical bold', 5), bg='white')

refButton = Button(win, image=referenceIcon,command= TakeReferenceImage,borderwidth=0, highlightthickness=0
    , height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg='white')
refButton.pack(pady=0, side=LEFT, anchor=N)


# Run program button  -------------------------------------------------------------------
runIcon = PhotoImage(file='/home/pearpi/Desktop/runProgram.gif')
runIcon = runIcon.subsample(2, 2)

runProgramLabel = Label(image=runIcon)
runProgramLabel.config(font=('Helvatical bold', 5), bg='white')

runButton = Button(win, image=runIcon,command= RunProgram,borderwidth=0, highlightthickness=0
    , height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg='white')
runButton.place(x=580,y=280)

# Exit program button  -------------------------------------------------------------------
exitIcon = PhotoImage(file='/home/pearpi/Desktop/iconExit.gif')
exitIcon = exitIcon.subsample(2, 2)

exitLabel = Label(image=exitIcon)
exitLabel.config(font=('Helvatical bold', 5), bg='white')

exitButton = Button(win, image=exitIcon,command=clickExitButton,borderwidth=0, highlightthickness=0
    , height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg='white')
exitButton.pack(pady=0, side=LEFT, anchor=N)


# Time Delay Button(s)  --------------------------------------------------------------------

TimeDelayAddImage = PhotoImage(file='/home/pearpi/Desktop/add.gif')
TimeDelayAddImage = TimeDelayAddImage.subsample(2, 2)

timeDelayLabel = Label(image=TimeDelayAddImage)
timeDelayLabel.config(font=('Helvatical bold', 5), bg='white')

timeDelayAddButton = Button(win, image=TimeDelayAddImage,command= TimeDelayAdd, borderwidth=0, highlightthickness=0,
    height=100, width=100, bg='white')
timeDelayAddButton.place(x=670, y=120)


TimeDelaySubImage = PhotoImage(file='/home/pearpi/Desktop/subtract.gif')
TimeDelaySubImage = TimeDelaySubImage.subsample(2, 2)

timeDelayLabel = Label(image=TimeDelaySubImage)
timeDelayLabel.config(font=('Helvatical bold', 5), bg='white')

timeDelaySubButton = Button(win, image=TimeDelaySubImage,command= TimeDelaySub, borderwidth=0, highlightthickness=0
    , height=100, width=100, bg='white')
timeDelaySubButton.place(x=540, y=120)



############################################################
##                      Slider                            ##
############################################################
slider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=Slider
    , sliderlength=50, length=400, bg='white', showvalue=False)
slider.place(x=20, y=355)



############################################################
##                      Labels                            ##
############################################################

display = Label(win, text="Detail", font=('Helvetica bold', 25), bg='white')
display.place(x=30, y=250)

thresRange = Label(win, text="(0-100)", font=('Helvetica bold', 10), bg='white')
thresRange.place(x=50, y=300)

displayThreshold = Label(win, text=f"{THRESHOLD}", font=('Helvetica bold', 40), bg='white')
displayThreshold.place(x=170, y=240)

timeDelayDisplay = Label(win, text=f"{TIMEDELAY}", font=('Helvetica bold', 40), bg='white')
timeDelayDisplay.place(x=635, y=35)

timeLabel = Label(win, text="Time Delay", font=('Helvetica bold', 15), bg='white')
timeLabel.place(x=600, y=10)

win.mainloop()

