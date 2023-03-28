import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


root=Tk()
root.title("TEXT TO SPEECH")
root.geometry("900x450")
root.resizable(False,False)
root.config(bg="#305065")



engine=pyttsx3.init()

def speaknow():
    text = text_area.get(1.0,END)
    gender=gender_Combobox.get()
    speed=speed_combobox.get()
    voice=engine.getProperty('voices')

    def setvoice():
        if(gender =='Male'):
            engine.setProperty('voice',voice[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voice[1].id)
            engine.say(text)
            engine.runAndWait()
    
    if (text):

        if(speed=='Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

#backend part
def savenow():                                  
    text = text_area.get(1.0,END)
    gender=gender_Combobox.get()
    speed=speed_combobox.get()
    voice=engine.getProperty('voices')

    def setvoice():
        if(gender =='Male'):
            engine.setProperty('voice',voice[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voice[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    
    if (text):

        if(speed=='Fast'):
            engine.setProperty('rate',220)
            setvoice()
        
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        
        else:
            engine.setProperty('rate',80)
            setvoice()

    

#frontend part

#icon
image_icon=PhotoImage(file="D:\\5th Sem\\Python Project\\1435843-200.png")
root.iconphoto(False,image_icon)

#top frame
Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

#logo and Name
Logo=PhotoImage(file="D:\\5th Sem\\Python Project\\unnamed (1).png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)

Label(Top_frame,text="TEXT TO SPEECH",font="impact 24 bold",bg="white",fg="#1270a4").place(x=120,y=30)

#text area for writing texts
text_area=Text(root,font="Roboto20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=120,width=500,height=250)

#voice and speed heading
Label(root,text="VOICE",font="ariel 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="ariel 15 bold",bg="#305065",fg="white").place(x=740,y=160)

#dropdown combobox
gender_Combobox=Combobox(root,values=['Male','Female'],font="ariel 14",state='r',width=8)
gender_Combobox.place(x=560,y=200)
gender_Combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="ariel 14",state='r',width=8)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

#buttons
img_icon=PhotoImage(file="D:\\5th Sem\\Python Project\\speaking-iconxx.png")
btn=Button(root,text="SPEAK",compound=LEFT,image=img_icon,width=105,font="ariel 11 bold",command=speaknow)
btn.place(x=560,y=280)

img_icon2=PhotoImage(file="D:\\5th Sem\\Python Project\\save-file-buttonxx.png")
btn_save=Button(root,text="SAVE",compound=LEFT,image=img_icon2,width=105,bg="green",font="ariel 11 bold",command=savenow)
btn_save.place(x=731,y=280)


root.mainloop()