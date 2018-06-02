# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:18:58 2018

@author: hp
"""
import socket
import speech_recognition as sr
import webbrowser
import datetime
import calendar
# import sys
import os
import ctypes
import cv2
#module for text to specch for windows
import win32com.client as wincl


mic = sr.Microphone()
r = sr.Recognizer()
speak = wincl.Dispatch("SAPI.SpVoice")

# Registering and getting Chrome to use as webbrowser
chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path), 1)
chrome = webbrowser.get('chrome')

# INITIAL OPTION. Asking User as given choice choose one out of the following functions of the program
print("\nHey there. What would you like to do today? Say either \"Google Something\" or \"Birthday\" or \"notepad\" or \"excel\" or \"powerpoint\" or \"paint\" or \"msword\".")
print(speak.Speak("hii i am ultron"))
with mic as audio_source:
    choice_of_function_voice_input = r.listen(audio_source)

try:
    what_user_said = r.recognize_google(choice_of_function_voice_input)
    # handle the exceptions
except sr.UnknownValueError:
    
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
 


def google_something():
    with mic as source:
        voice_input = r.listen(source)
        try:
            print("Googling \"{}\"...".format(str(r.recognize_google(voice_input))))
            chrome.open_new_tab('http://www.google.com/search?btnG=1&q={}'.format(str(r.recognize_google(voice_input))))

        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")


def notepad():
    with mic as source:
        
        voice_input = r.listen(source)
        try:
            os.startfile("C:\Windows\System32\\notepad.exe")
        
        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")
            
def msword():
    with mic as source:
        voice_input = r.listen(source)
        try:
            os.startfile("C:\Program Files (x86)\Microsoft Office\Office14\WINWORD.exe")
        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")
            


def msexcel():
    with mic as source:
        voice_input = r.listen(source)
        try:
            os.startfile("C:/Program Files (x86)/Microsoft Office/Office14/EXCEL.exe")
        
        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")


def msppt():
    with mic as source:
        voice_input = r.listen(source)
        try:
            os.startfile("C:\Program Files (x86)\Microsoft Office\Office14\POWERPNT.exe")

        
        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")

def msaccess():
    with mic as source:
        voice_input = r.listen(source)
        try:
            os.startfile("C:\Program Files (x86)\Microsoft Office\Office14\MSACCESS.exe")

        
        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")

def mspaint():
    with mic as source:
        voice_input = r.listen(source)
        try:
            
            os.startfile("C:\Windows\System32\mspaint.exe")
        
        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")

def onenote():
    with mic as source:
        voice_input = r.listen(source)
        try:
            os.startfile("C:/Program Files (x86)/Microsoft Office/Office14/ONENOTE.exe")
        
        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")

#system application access

def cmd():
    with mic as source:
        voice_input = r.listen(source)
        try:
            os.startfile("C:\Windows\System32\cmd.exe")
        
        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")
def Cpanel():
    with mic as source:
        voice_input = r.listen(source)
        try:
            os.startfile("C:\Windows\System32\control.exe")
        
        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")
def bluetooth():
    with mic as source:
        voice_input = r.listen(source)
        try:
            os.startfile("C:\Windows\System32\fsquirt.exe")
        
        except sr.UnknownValueError:
            print(sr.UnknownValueError)
            print("Something went wrong.")











def get_birthday_weekday():
    """To figure out what weekday User's birthday is this year, three variables are needed - year, month and date.
    The year is the same for every User, and declared in the beginning of the function."""
    year = 2018

    # MONTH
    """Asking User what month they are born, and listening for an answer. If their voice input matches one of the strings
    (name of months) in the dictionary, the "month" variable gets set to the corresponding number."""
    with mic as source:
        print("What month are you born?")
        birthday_month_voice_input = r.listen(source)
        interpreted_month = str(r.recognize_google(birthday_month_voice_input))

        months = {"January": 1,
                  "February": 2,
                  "March": 3,
                  "April": 4,
                  "May": 5,
                  "June": 6,
                  "July": 7,
                  "August": 8,
                  "September": 9,
                  "October": 10,
                  "November": 11,
                  "December": 12,
                  }

    for m in months:
        if interpreted_month == m:
            month = months.get(m)
            print(month)

        '''I wanted to have a backup in the case User says a word that is not a month. However, with this code uncommented,
         the program does not accept the name of the months as valid either. '''
         #   else:
         #       print("Didn't get a month. Restart and try again.")
         #       sys.exit()

    # DATE
    with mic as source:
        print("What date are you born? Please say it as a number, for instance \"Seven\" \nor \"Twentythree\".")
        birthday_date_input = r.listen(source)
        date = r.recognize_google(birthday_date_input)

        # A correction to recognize_google()'s way of printing the first few numbers out with letters:
        if date == "one" or date == "first":
            date = 1
        elif date == "two" or date == "second":
            date = 2
        elif date == "three":
            date = 3
        print(date)

        birthday = datetime.date(year, month, int(date))

        birthday_weekday = calendar.day_name[birthday.weekday()]
        print("*** This year your birthday is on a " + birthday_weekday + ". ***")


if str(what_user_said) == "Google something":
    print("Tell me what you want to google?")
    google_something()

elif str(what_user_said) == "birthday":
    print("Checking what weekday your birthday is 2018.")
    get_birthday_weekday()
    
elif str(what_user_said)== "notepad":
    print("lauching notepad !!")
    notepad()
elif str(what_user_said)== "msexcel":
    print("lauching excel !!")
    msexcel()
elif str(what_user_said)== "msword":
    print("lauching msword !!")
    msword()
elif str(what_user_said)== "ppoint":
    print("lauching powerpint !!")
    msppt()
elif str(what_user_said)== "paint":
    print("lauching paint !!")
    mspaint()
elif str(what_user_said)== "lock":
    print("wait your pc about to lock!!")
    ctypes.windll.user32.LockWorkStation()
            
elif str(what_user_said)== "msaccess":
    print("lauching MSAccess !!")
    msaccess()
elif str(what_user_said)== "onenote":
    print("lauching oneNote !!")
    onenote()
elif str(what_user_said)== "terminal":
    print("lauching cmd!!")
    print(speak.Speak("lauching cmd !!"))
    cmd()
elif str(what_user_said)== "control panel":
    print("lauching control panel !!")
    Cpanel()
elif str(what_user_said)== "bluetooth":
    print(speak.Speak("lauching bluetooth !!"))
    bluetooth()
elif str(what_user_said)== "ping":
    print("lauching ping !!")
    os.startfile("C:\Windows\System32\PING.exe")
elif str(what_user_said)== "explorer":
    print("lauching explorer !!")
    os.startfile("C:\Windows\explorer.exe") 
    bluetooth()
elif str(what_user_said)== "clculator":
    print("lauching calc !!")
    os.startfile("C:\Windows\System32\calc.exe")

#access ip adress
elif str(what_user_said)== "address":
     print("Want to get IP Address ? (yes/no): ")
     if str(what_user_said)== 'no':
         exit()
     else:
         print("\nYour IP Address is: ",end="");
         print(socket.gethostbyname(socket.gethostname()));
#acess camera face detection using opencv
elif str(what_user_said)== "camera":
    print("opening camera for facedetection")
    print(speak.Speak("opening camera for facedetection"))
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('tiyle',gray)
        if cv2.waitKey(1) & 0XFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

else:
    print("Try again.")
