#####################################
# Author: Sarah Fox
# Created on: 11/09/2019
# Programming Fundamentals
# Filename: hw-5-6.py
# Purpose: A program that encodes the text a user input
#####################################

'''
START
    Create comment header
    Import graphics library
    Import math library 
    Get 15 character input from user using Entry Object
    Encrypt each letter using the ord method multiplied by a digit from the value of Pi
    Ask for user to click window
    Print encoded message once window is clicked
    Close window with another click input from user
END
'''
from graphics import *
import math

def main():
    win = GraphWin("Encoded Message",500,500)
    win.setCoords(0,0,500,500)
    win.setBackground("cyan")

    message = Text(Point(250,310),"Please Enter a Message to Encode: ")
    message.draw(win)
    message.setSize(14)
    #message.setFace("times roman")
    message.setStyle("italic")

    userInput = Entry(Point(250,280),15)
    userInput.draw(win)
    win.getMouse() # Need this in order to grab text otherwise the entry object will be empty and the .getText() will pull from entry before I enter text

    inputText = userInput.getText()

    piNumbers = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
    encryptedList = []
    ## Encryption
    index = 0 # This works as a counter to index through piNumbers list 
    for i in inputText:
        encryptedList.append(ord(i)*piNumbers[index])
        index = index + 1 # This is a counting loop so it will go 0,1,2,3 by adding 1 on each iteration (i)

    strEncryptedList = ""    
    for i in encryptedList:
        strEncryptedList = strEncryptedList + " " + str(i)

    message2 = Text(Point(250,220),"Your Encoded Message Is: ").draw(win)
    message2.setSize(14)
    message2.setStyle("bold italic")
    #message2.setTextColor("blue")

    message3 = Text(Point(250,190), encryptedList).draw(win)
    message3.setSize(14)
    print(message3)

    win.getMouse()
    win.close()
main()

