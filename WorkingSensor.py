############################################################
##                        Imports                         ##
############################################################
import subprocess
import sys
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
# import easygui
# import wiringp

from tkinter import *
from time import sleep
from PIL import Image, ImageChops, ImageOps
from gpiozero import LightSensor, Buzzer
from numpy import sum, average
from picamera import PiCamera
# from scipy.linalg import norm
# from matplotlib.pyplot import imread

############################################################
##                      Global Variables                  ##
############################################################

# Primitive variables -------------------------------
THRESHOLD = 0
REVTHRESHOLD = 0
TIMEDELAY = 0
NEWTIMEDELAY = 0
BUTTON_HEIGHT = 150
BUTTON_WIDTH = 150
INDEX = 0
BUZZER = Buzzer(17)
RUNNING = False

# GPIO variables -----------------------------------
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
# GPIO.setwarnings(False)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

############################################################
##                Image Operations                        ##
############################################################

def ReverseThreshold(thres):
    global REVTHRESHOLD
    result = 0
    while (thres < 100):
        result += 1
        thres += 1
    REVTHRESHOLD = result
    
 # ----------------------------------------------------------------

def CompareImages():
    global INDEX, REVTHRESHOLD, THRESHOLD, BUZZER
    
    INDEX = 0
    thres = int(THRESHOLD)
    ReverseThreshold(thres)
    thres = int(REVTHRESHOLD)

    img1 = cv2.imread("/home/pearpi/Desktop/Images/ref.jpg")
    img2 = cv2.imread("/home/pearpi/Desktop/Images/pic"+str(INDEX)+".jpg")
#   img2 = img2.resize(img1.size)

    # convert the images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # compute MSE between two images
    def mse(img1, img2):
        h, w = img1.shape
        diff = cv2.subtract(img1, img2)
        err = np.sum(diff**2)
        mse = err/(float(h*w))
        return mse, diff

    error, diff = mse(img1, img2)
    print("Image matching Error between the two images:",error)
    
    if error > thres:
        diff = cv2.resize(diff, (750,400))
        BUZZER.on()
        cv2.imshow("difference", diff)
        cv2.waitKey(0)
        BUZZER.off()
        cv2.destroyAllWindows()

 # ----------------------------------------------------------------
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
     
    # set Trigger after 0.01ms to LOW
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
    print("--- Calculating Time ---")
    
    # save StartTime
    try:
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
    except TimeoutException:
        print("Echo Pin is broken")
    
    # save time of arrival
    try:
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time() 
    except TimeoutException:
        print("Echo Pin is alive")
    
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

# ----------------------------------------------------------------

def captureImage():
    global INDEX
    subprocess.call((['raspistill -o /home/pearpi/Desktop/Images/pic'+str(INDEX)+'.jpg']),shell=True)

   
############################################################
##                      Main                              ##
############################################################

def startProgram():
    global TIMEDELAY, RUNNING, THRESHOLD
    RUNNING = True

    try:
        idx = 0
        while True:
            if idx % 1 == 0:
                win.update()
                print("--- Updating root Task ---")
                if (RUNNING == False):
                    print("--- Program is no longer running ---")
                
            if RUNNING:
                idx += 1
                dist = distance()
                print ("Measured Distance = %.1f cm" % dist)
                if (dist > 200):
                    sleep(TIMEDELAY)
                    captureImage()
                    CompareImages()
                time.sleep(0.5)
            else:
                print("--- Breaking Program ---")
                break

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()


# --------------------------------------------------
############################################################
##                      Window                            ##
############################################################

win=Tk()
win.geometry("1050x535")
win.config(bg='white')
win.wm_title("Pear Pi")


############################################################
##                   UI Functions                         ##
############################################################

# Run Sensor & Image Conversion
def RunProgram():
    global RUNNING
    
    if (RUNNING):
        RUNNING = False
    else:
        RUNNING = True
        print("--- Running program ---")
        startProgram()

# Exit the program entirely
def clickExitButton():
    sys.exit()
    #root.destory()


# Allows the user to see what the camera sees temporarily
# ----------------------------------------------------------------
def PositionCamera():
    print("*** Turning on the camera ***")
    camera = PiCamera()
    camera.start_preview()
    sleep(10)
    camera.stop_preview()
    camera.close()

 # ----------------------------------------------------------------
 
 # Takes reference image to compare once program is started
def TakeReferenceImage():
    print("*** Taking reference Image ***")
    subprocess.call((['raspistill -o /home/pearpi/Desktop/Images/ref.jpg']),shell=True)

# ----------------------------------------------------------------

# Controls the slider UI logic
def Slider(val):
    global THRESHOLD
    THRESHOLD = val
    displayThreshold.config(text=f'{THRESHOLD}')

# ----------------------------------------------------------------
 
 # Adds time to the time delay feature
def TimeDelayAdd():
    global TIMEDELAY
    if TIMEDELAY >= 0:
        TIMEDELAY = TIMEDELAY + 1
        timeDelayDisplay.config(text=f'{TIMEDELAY}')

    if TIMEDELAY < 10:
        timeDelayDisplay.config(timeDelayDisplay.place(x=840, y=65))
    else:
        timeDelayDisplay.config(timeDelayDisplay.place(x=820, y=65))

# ----------------------------------------------------------------

# Subtracts time from the time delay feature
def TimeDelaySub():
    global TIMEDELAY
    if TIMEDELAY > 0:
        TIMEDELAY = TIMEDELAY - 1
        timeDelayDisplay.config(text=f'{TIMEDELAY}')

    if TIMEDELAY < 10:
        timeDelayDisplay.config(timeDelayDisplay.place(x=840, y=65))
    else:
        timeDelayDisplay.config(timeDelayDisplay.place(x=815, y=65))

# ----------------------------------------------------------------


############################################################
##                      Image Buttons                     ##
############################################################

# Position button  ---------------------------------------------------------------------
positionIcon = PhotoImage(file='/home/pearpi/Desktop/position.gif')
#positionIcon = positionIcon.subsample(2, 2)

positionLabel = Label(image=positionIcon)
positionLabel.config(font=('Helvatical bold', 10), bg='white')

positionButton= Button(win, image=positionIcon,command= PositionCamera,borderwidth=0, highlightthickness=0
    , height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg='white')
positionButton.place(x=0,y=10)


# Reference Image Button  ---------------------------------------------------------------
referenceIcon = PhotoImage(file='/home/pearpi/Desktop/camera.gif')
#referenceIcon = referenceIcon.subsample(2, 2)

referenceLabel = Label(image=referenceIcon)
referenceLabel.config(font=('Helvatical bold', 5), bg='white')

refButton = Button(win, image=referenceIcon,command= TakeReferenceImage,borderwidth=0, highlightthickness=0
    , height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg='white')
refButton.place(x=220,y =10)


# Run program button  -------------------------------------------------------------------
runIcon = PhotoImage(file='/home/pearpi/Desktop/runProgram.gif')
runIcon = runIcon.subsample(2, 2)

runProgramLabel = Label(image=runIcon)
runProgramLabel.config(font=('Helvatical bold', 5), bg='white')

runButton = Button(win, image=runIcon,command= RunProgram,borderwidth=0, highlightthickness=0
    , height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg='white')
runButton.place(x=800,y=300)

# Exit program button  -------------------------------------------------------------------
exitIcon = PhotoImage(file='/home/pearpi/Desktop/iconExit.gif')
#exitIcon = exitIcon.subsample(2, 2)

exitLabel = Label(image=exitIcon)
exitLabel.config(font=('Helvatical bold', 5), bg='white')

exitButton = Button(win, image=exitIcon,command=clickExitButton,borderwidth=0, highlightthickness=0
    , height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg='white')
exitButton.place(x=450,y =10)


# Time Delay Button(s)  --------------------------------------------------------------------

TimeDelayAddImage = PhotoImage(file='/home/pearpi/Desktop/add.gif')
TimeDelayAddImage = TimeDelayAddImage.subsample(2, 2)

timeDelayLabel = Label(image=TimeDelayAddImage)
timeDelayLabel.config(font=('Helvatical bold', 5), bg='white')

timeDelayAddButton = Button(win, image=TimeDelayAddImage,command= TimeDelayAdd, borderwidth=0, highlightthickness=0,
    height=100, width=100, bg='white')
timeDelayAddButton.place(x=870, y=135)


TimeDelaySubImage = PhotoImage(file='/home/pearpi/Desktop/subtract.gif')
TimeDelaySubImage = TimeDelaySubImage.subsample(2, 2)

timeDelayLabel = Label(image=TimeDelaySubImage)
timeDelayLabel.config(font=('Helvatical bold', 5), bg='white')

timeDelaySubButton = Button(win, image=TimeDelaySubImage,command= TimeDelaySub, borderwidth=0, highlightthickness=0
    , height=100, width=100, bg='white')
timeDelaySubButton.place(x=740, y=135)



############################################################
##                      Slider                            ##
############################################################

slider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=Slider
    , sliderlength=50, length=400, bg='white', showvalue=False)
slider.place(x=20, y=450)



############################################################
##                      Labels                            ##
############################################################

display = Label(win, text="Detail", font=('Helvetica bold', 30), bg='white')
display.place(x=30, y=350)

thresRange = Label(win, text="(0-100)", font=('Helvetica bold', 18), bg='white')
thresRange.place(x=50, y=400)

displayThreshold = Label(win, text=f"{THRESHOLD}", font=('Helvetica bold', 50), bg='white')
displayThreshold.place(x=170, y=350)

timeDelayDisplay = Label(win, text=f"{TIMEDELAY}", font=('Helvetica bold', 40), bg='white')
timeDelayDisplay.place(x=840, y=65)

timeLabel = Label(win, text="Time Delay", font=('Helvetica bold', 25), bg='white')
timeLabel.place(x=775, y=10)

win.mainloop()
