#SUJIT KUMAR SAHOO (20BCS9626)
#JUVERIYAH (20BCS9621)
#NAVJOT SINGH TALWANDI (20BCS9598)
#ASHISH PRAJAPATI (20BCS9625)


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text2Speech")
root.geometry("1000x650+250+250")
root.resizable(False,False)
root.configure(bg="#EB984E")

engine= pyttsx3.init()


def speaknow():
    text=text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender == 'MALE'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if(speed =="FAST"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == 'NORMAL'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
            
def download():
     text=text_area.get(1.0,END)
     gender = gender_combobox.get()
     speed = speed_combobox.get()
     voices = engine.getProperty('voices')

     def setvoice():
         if(gender == 'MALE'):
             engine.setProperty('voice', voices[0].id)
             path=filedialog.askdirectory()
             os.chdir(path)
             engine.save_to_file(text, 'text.mp3')
             engine.runAndWait()
         else:
             engine.setProperty('voice', voices[1].id)
             path=filedialog.askdirectory()
             os.chdir(path)
             engine.save_to_file(text, 'text.mp3')
             engine.runAndWait()
     if(text):
         if(speed =="FAST"):
             engine.setProperty('rate',250)
             setvoice()
         elif(speed == 'NORMAL'):
             engine.setProperty('rate',150)
             setvoice()
         else:
             engine.setProperty('rate',60)
             setvoice()

#ICON
image_icon=PhotoImage(file="D:/PROJECT 4TH SEM/speak.png")
root.iconphoto(False,image_icon)

#TOP FRAME 
Top_frame=Frame(root,bg="white", width=1000,height=100)
Top_frame.place(x=0,y=0)

#LOGO
Logo=PhotoImage(file="D:/PROJECT 4TH SEM/Text to Speech.png")
Label(Top_frame,image=Logo,bg="white").place(x=5,y=5)

#TITLE
Label(Top_frame,text="WORD TALK", font="arial 30 bold",bg="white", fg="black").place(x=100,y=30)
                

text_area=Text(root,font="arial 12",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=400)

Label(root,text="VOICE",font="arial 18 bold", bg="#EB984E", fg="white").place(x=580, y=160)
Label(root,text="SPEED",font="arial 18 bold", bg="#EB984E", fg="white").place(x=760, y=160)

#GENDER VOICE
gender_combobox=Combobox(root,values=['MALE','FEMALE'],font="arial 18",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('MALE')

#AUDIO SPEED
speed_combobox=Combobox(root,values=['FAST','NORMAL','SLOW'],font="arial 18",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('NORMAL')

#SPEAK BUTTON
imageicon=PhotoImage(file="D:/PROJECT 4TH SEM/speak.png")
btn=Button(root,text="SPEAK",compound=LEFT,image=imageicon,width=150,font="arial 18 bold",command=speaknow)
btn.place(x=550,y=280)

#SAVE AUDIO BUTTON
imageicon2=PhotoImage(file="D:/PROJECT 4TH SEM/Save.png")
save=Button(root,text="SAVE",compound=LEFT,image=imageicon2,width=150,font="arial 18 bold",command=download)
save.place(x=730,y=280)


root.mainloop()
