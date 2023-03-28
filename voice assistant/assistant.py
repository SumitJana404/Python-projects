import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
import random


def speech2text():                    #function
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)

        try:
            print("Recognizing")
            data=recognizer.recognize_google(audio)
            #print(data)
            return data
        except sr.UnknownValueError:
            print("Unable to recognize")
#speech2text()

def text2speech(x):                   #function
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
#txt=input("Enter Your text here : ")
#text2speech(txt)



if __name__ == '__main__':

    if "lisa" in speech2text().lower():

        while True:
            
            data1=speech2text().lower()

            if "your name" in data1:
                name="my name is lisa"
                text2speech(name)
                
            elif "old are you" in data1 or "your age" in data1:
                age="i am eighteen years old"
                text2speech(age)
            
            elif "developed you" in data1 or "made you" in data1:
                developed_by="sumit "
                text2speech(developed_by)

            elif "are you from" in data1:
                whr_r_u_frm="I am from your heart"
                text2speech(whr_r_u_frm)
            
            elif "have a boyfriend" in data1 or "any boyfriend" in data1:
                bf="yes i do, and his name is sumit"
                text2speech(bf)
            
            #elif "you are sexy" in data1:
                #how_sexy="thank you"
                #text2speech(how_sexy)
            
            elif "how are you" in data1:
                how_am_i="i am good, and you"
                text2speech(how_am_i)
            elif "fine" in data1:
                how_am_i_reply="oh good"
                text2speech(how_am_i_reply)

            elif "the time" in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                text2speech(time)

            elif "open youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
                
            elif "open wikipedia" in data1:
                webbrowser.open("https://www.wikipedia.org/")

            elif "open insta" in data1 or "open instagram" in data1:
                webbrowser.open("https://www.instagram.com/sumitjana_/?fbclid=IwAR3Ogy2VmP1UnsqFQyBpNx1kh4XwFvGgkaZXWfrTZrME7usDsG7DQahovps")

            elif "open facebook" in data1:
                webbrowser.open("https://www.facebook.com/")
            

            elif "jokes" in data1:
                joke1=pyjokes.get_joke(language="",category="neutral")
                text2speech(joke1)
                
            elif "play songs" in data1:
                add="E:\songs" 
                listsong=os.listdir(add)
                print(listsong)
                a=random.randint(0,110)
                os.startfile(os.path.join(add,listsong[a]))
                
            elif "exit" in data1:
                text2speech("thank you")
                break
            #time.sleep(3)
                 
    else:
        print("Wake up call did not matched")


