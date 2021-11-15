import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import os
from time import ctime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def jarvisSpeak(audio_string):
    try:
        engine.say(audio_string)
        engine.runAndWait()
        engine.setProperty('rate', 175)
        return True
    except:
        t = "Sorry I couldn't understand and handle this input"
        print(t)
        return False

def jarvis():
    voice_jarvis = 'hello i\'m jarvis 2.0'\
                 ' created by Lovelyo Yeremia Mokalu'
    jarvisSpeak(voice_jarvis)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        jarvisSpeak('Good morning Lovelyo!')
    elif hour >= 12 and hour < 18:
        jarvisSpeak('Good Afternoon Lovelyo!')
    else:
        jarvisSpeak('Good Evening Lovelyo!')

    jarvisSpeak('I am Online and ready to help you, please tell me what you need ,and i will do as you wish')

def recordAudio():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')  
            r.energy_threshold = 4000
            audio = r.listen(source)
            voice_data = ''
            try: 
                print('Recognizing...')        
                voice_data = r.recognize_google(audio,language='en').lower()
                print('user said:' + voice_data)
            except sr.UnknownValueError:
                jarvisSpeak('sorry, i didn\'t get that')
                voice_data = recordAudio()
            except sr.RequestError:
                jarvisSpeak('sorry, my speech service is down')
            return voice_data
    except Exception as e:
        print(e)
        return False

def respond(voice_data):

    while True:

        # '''Jokes'''
        if 'what is your name' in voice_data:
            jarvisSpeak('my name is Jarvis sir, your personal assistant sir,'\
                        ' How come you forget my name,sir?')
            
        
        elif 'who am I' in voice_data:
            jarvisSpeak('i\'m sorry i forget sir hahahahahahahahaha?')
            

        elif 'jarvis jarvis' in voice_data:
            jarvisSpeak('yes sir, how may i help you?')
            
        
        elif 'yes' in voice_data:
            jarvisSpeak('but you don\'t have enough money sir hahahahahahahaha')
            
        elif 'no jarvis' in voice_data:
            jarvisSpeak('i am sorry sir, i\'m just curious')
            

        elif 'sing' in voice_data:
            jarvisSpeak('''twinkle twinkle little star,
                        how i wonder what you are. up above, the world, so high,like a diamond ,in the sky,
                        twinkle twinkle little star,
                        how i wonder what you are .''')
            jarvisSpeak('i told you that i can\'t sing sir')
            

        elif 'break' in voice_data:
            jarvisSpeak('bye sir, wake me up if you need me anytime')
            exit()

        # '''ANYTHING'''
        elif 'code' in voice_data:
            path = 'C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(path)
            jarvisSpeak('here you go sir, enjoy!')
            

        elif 'make music' in voice_data:
            path = 'C:\\Program Files\\PreSonus\\Studio One 5\\Studio One.exe'
            os.startfile(path)
            jarvisSpeak('here you go sir,enjoy!')
            

        elif 'calculate' in voice_data:
            from features import calculator
            voice_data = voice_data.replace('calculate','')
            jarvisSpeak('Ok sir, let me think and i\'ll let you know if i\'ve found the answer')
            calculator(voice_data)
            

        elif 'spotify' in voice_data:
            jarvisSpeak('Ok sir, as you wish, i will open the spotify')
            path = 'C:\\Users\\user\\AppData\\Roaming\\Spotify\\Spotify.exe'
            os.startfile(path)
            
      
        elif 'wikipedia' in voice_data:
            from features import wikipediaSearch
            page = voice_data.replace('according to wikipedia','')
            result = 'https://en.wikipedia.org/wiki/' + page
            webbrowser.open(result)
            wikipediaSearch(voice_data)
            

        # '''YOUTUBE'''
        elif 'open youtube' in voice_data:
            jarvisSpeak('Ok sir, as you wish, i will open the youtube')
            url = 'https://youtube.com'
            webbrowser.open(url)
            
        
        elif 'play youtube' in voice_data:
            from features import youtubeSearch
            jarvisSpeak('what do you want to search for?')
            search = recordAudio()
            Voice_data = search.replace('youtube','')
            voice_data = search.replace('play','')
            youtubeSearch(Voice_data)
            

        # '''GOOGLE'''
        elif 'google' in voice_data:
            
            jarvisSpeak('Ok sir, as you wish, i will open the google')
            url = 'https://google.com'
            webbrowser.open(url)
            
        
        elif 'search' in voice_data:
            from features import googleSearch
            jarvisSpeak('what do you want to search for?')
            Voice_data = recordAudio()
            googleSearch(Voice_data)  
                  
        
        elif 'my location' in voice_data:
            from features import myLocation
            myLocation()
            
        
        elif 'where is' in voice_data:
            from features import googleMaps
            voice_data = voice_data.replace('where','')
            voice_data = voice_data.replace('is','')
            googleMaps(voice_data)
            
        
        # '''WHATSAPP'''
        elif 'send message' in voice_data:
            from automation import whatsappMessage
            name = voice_data.replace('whatsapp message','')
            name = voice_data.replace('send','')
            name = voice_data.replace('message','')
            name = voice_data.replace('to','')
            Name = str(name)
            jarvisSpeak(f'what\'s the message for {Name}')
            message = recordAudio()
            msg = message.replace('whatsapp message','')
            msg = msg.replace('send','')
            msg = msg.replace('message','')
            msg = msg.replace('to','')
            whatsappMessage(Name,msg)
            
        
        elif 'call' in voice_data: 
            from automation import whatsappCall
            name = voice_data.replace('call','')
            name = name.replace('jarvis','')
            Name = str(name)
            jarvisSpeak(f'as you wish i will call {Name}')
            whatsappCall(Name)
            
        
        elif 'show chat' in voice_data:
            from automation import whatsappOpenChat
            jarvisSpeak('with whom?')
            name = recordAudio()
            whatsappOpenChat(name)
            

        elif 'video call' in voice_data:
            from automation import whatsappVideoCall
            name = voice_data.replace('video call','')
            name = name.replace('to','')
            name = name.replace('jarvis','')
            Name = str(name)
            jarvisSpeak(f'as you wish, i will call {Name}')
            whatsappVideoCall(Name)
            
        
        # '''NASA'''
        elif 'space news' in voice_data:
            from features import dateConverter
            jarvisSpeak('what date do you want to know about? ')
            date = recordAudio()
            Date = dateConverter(date)
            from nasa import nasaNews
            nasaNews(Date)
            

        elif 'about' in voice_data:
            from features import wolfRam
            voice_data = voice_data.replace('i just','')
            voice_data = voice_data.replace('want to know','')
            voice_data = voice_data.replace('about','')
            voice_data = voice_data.replace('jarvis','')
            wolfRam(voice_data)
            

        # '''TIME AND CONDITION'''
        elif 'time' in voice_data:
            jarvisSpeak(ctime())
            
  
        elif 'set alarm' in voice_data:
            from features import alarmSet
            alarmSet(voice_data)
            
   
        elif 'temperature' in voice_data:
            from features import temperature
            temperature(voice_data)
            

        # '''EXIT'''
        elif 'exit' in voice_data:
            jarvisSpeak('bye sir')
            exit() 

    # return voice_data

if __name__ == '__main__':
    voice_data = recordAudio()
    respond(voice_data)