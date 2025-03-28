import pyttsx3
import speech_recognition as spr
import datetime
import wikipedia
import pyjokes
import pyaudio
import random
import webbrowser
import imaplib
import email
import os
import smtplib
import ctypes
import urllib.request
import re
from pytube import YouTube
from time import sleep
from pyautogui import click
from keyboard import press
from keyboard import write
from os import startfile
import geocoder

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("Gideon at you service, How can i help you!")


def takeCommand():
    r = spr.Recognizer()
    with spr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    user = open("user.txt", "r")
    cred1 = user.readline()
    password = open("pass.txt", "r")
    cred2 = password.readline()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(cred1, cred2)
    server.sendmail(cred1, emails[to], content)
    server.close()


def whatsappmsg(name, msg):
    startfile("C:\\Users\\9myst\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    click(x=202, y=145)
    sleep(0.5)
    write(name)
    sleep(1)
    click(x=200, y=305)
    sleep(2)
    click(x=819, y=998)
    write(msg)
    press('enter')


def get_inbox():
    host = 'imap.gmail.com'
    username = 'username'
    password = 'password'
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject']:
            s = ("{}: {}".format(header, email_message[header]))
        l = s[9:]
        webbrowser.open(l)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif 'open whatsapp' in query:
            whatsapppath = "C:\\Users\\9myst\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsapppath)

        elif 'play music' in query:
            musicfolder = 'U:\\Personal\\musicfolder'
            songs = os.listdir(musicfolder)
            os.startfile(os.path.join(musicfolder, songs[0]))
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\9myst\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'send an email' in query:
            try:
                emails = {"o n e": "mail_1", "t w o": "mail_2"}
                speak("Whom do you want to send the mail?")
                print(emails)
                to = takeCommand()
                speak("What do you want to say!")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry sir. I am not able to send this email")

        elif 'sleep now' in query:
            speak("Hope you have a good day sir!")
            exit()

        elif 'send a whatsapp message' in query:
            try:
                speak("To, who!")
                name = takeCommand()
                speak("What do you want to say!")
                msg = takeCommand()
                whatsappmsg(name, msg)
                speak("Message sent successfully!")
            except Exception as e:
                speak("Sorry sir. I am not able to send this message")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'weather' in query:
            speak("Please wait a second sir!")
            g = geocoder.ip('me')
            address = ' '.join(str(elem) for elem in g)
            s = address.split()[0]
            l = s[1:-1]
            webbrowser.open("https://www.google.com/search?q=weather+of+" + l)


        elif 'song' in query:
            speak("What song would you like me to download!")
            search_keyword = takeCommand()
            z = "+".join(search_keyword.split())
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + z)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            URL = ("https://www.youtube.com/watch?v=" + video_ids[0])
            yt = YouTube(URL)
            my_video = YouTube(URL)
            my_video = my_video.streams.get_highest_resolution()
            speak("Downloading... Please Wait!")
            my_video.download("C:\\Users\\9myst\\Desktop\\New folder\\Gideon\\Personal\\musicfolder")
            speak("Download Complete!...")

        elif 'check' in query:
            try:
                while True:
                    get_inbox()
            except KeyboardInterrupt:
                pass

        elif 'toss' in query:
                moves = ["head", "tails"]
                cmove = random.choice(moves)
                speak("It is" + cmove +"this time")

# code for checking the click co-ordinates on the screen.
"""
import pyautogui
from time import sleep
sleep(10)
loc=pyautogui.position()
print(loc)

"""
