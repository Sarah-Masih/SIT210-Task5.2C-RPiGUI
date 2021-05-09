#References for code is from youtube: https://www.youtube.com/watch?v=ap-ABFNCBoE and https://www.tutorialspoint.com/
from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#Hardware

Red=LED(14)
Blue=LED(15)
Green=LED(18)

#gui defination

win=Tk()  #win is short for window
win.title("LED Toggler")
myFont = tkinter.font.Font(family='Helvetica', size = 12, weight = 'bold')
frame=Frame(win)
frame.pack()
bottomframe = Frame(win)
bottomframe.pack( side = BOTTOM )

#event functions

def RedToggle():
    Red.on()
    Green.off()
    Blue.off()

def GreenToggle():
    Green.on()
    Red.off()
    Blue.off()
def BlueToggle():
    Blue.on()
    Red.off()
    Green.off()
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
var=IntVar() 

#WIDGETS

RedButton= Radiobutton(win, text="Turn Red LED on", variable=var, value=1,command=RedToggle)
RedButton.pack( anchor = W )
GreenButton= Radiobutton(win, text="Turn Green LED on", variable=var, value=2,command=GreenToggle)
GreenButton.pack( anchor = W )
BlueButton= Radiobutton(win, text="Turn Blue LED on", variable=var, value=3,command=BlueToggle)
BlueButton.pack( anchor = W )

exitButton= Button(bottomframe, text="Exit", fg="white", command=close, bg='red')
exitButton.pack( side = BOTTOM)

win.protocol("WIN DELETE WINDOW", close)