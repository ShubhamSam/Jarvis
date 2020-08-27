import pyttsx3 #pip install pyttsx3
import datetime 
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
import smtplib

# Speech Application Programming Interface(SAPI)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sam')
    elif hour >= 12 and hour < 16:
        speak('Good Afternoon Sam')
    else:
        speak('Good Evening Shubham')
    speak('I am Jarvis. How may I help you')

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in') # This is a google engine used for taking audio input from user
        print(f'You said: {query}\n')
    except Exception:
        # print(e)
        print('Say that again please...')
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email', 'Your Password')
    server.sendmail('Your Email', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
         # Logic for exceuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open coursera' in query:
            webbrowser.open('coursera.com')
        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            song_rand = random.randrange(0, (len(songs)-1))
            os.startfile(os.path.join(music_dir, songs[song_rand]))
        elif 'play video' in query:
            video_dir = 'D:\\Videos'
            videos = os.listdir(video_dir)
            video_rand = random.randrange(0, (len(videos)-1))
            os.startfile(os.path.join(video_dir, videos[video_rand]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime('%m/%d/%Y')
            speak(f"Sir, the date is {strDate}")
        elif 'month' in query:
            strMonth = datetime.datetime.now().strftime('%B')
            speak(f'Sir current month is {strMonth}')
        elif 'code' in query:
            vs_Path = "C:\\Users\\Shubham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_Path)
        elif 'pycharm' in query:
            py_Path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.1\\bin\\pycharm64.exe"
            os.startfile(py_Path)
        elif 'open whatsapp' in query:
            whats_Path = 'C:\\Users\\Shubham\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
            os.startfile(whats_Path)

        elif 'email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "Receiver's Email"
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry Sam, Failed to send email')
        
        elif "exit" in query:
            exit()