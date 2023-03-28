from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


def change(text="type",src="english",dest="hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    masg=Sor_txt.get(1.0,END)
    textget=change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)



root=Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='#ADD8E6')

lab_txt1=Label(root,text="Translator",font=("Times New Roman",40,"bold"),fg="black",bg="orange")
lab_txt1.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_txt2=Label(root,text="Your Text",font=("Times New Roman",20,"bold"),fg="black",bg="#06c2ac")
lab_txt2.place(x=155,y=100,height=25,width=180)

Sor_txt=Text(frame,font=("Times New Roman",20,"bold"))
Sor_txt.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text)      #1st combo box
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("english")

button_change=Button(frame,text="Translate",relief=RAISED,command=data)      #button
button_change.place(x=170,y=300,height=40,width=150)

comb_dest=ttk.Combobox(frame,value=list_text)                     #2nd combobox
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

lab_txt3=Label(root,text="Translated Text",font=("Times New Roman",20,"bold"),fg="black",bg="orange")
lab_txt3.place(x=100,y=360,height=30,width=300)

dest_txt=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)



root.mainloop()