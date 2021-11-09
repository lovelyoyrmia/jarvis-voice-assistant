from playsound import playsound
import datetime

extracted_time = open('C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\Data.txt','rt')
time = extracted_time.read()
Time = str(time)

delete_time = open('C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\Data.txt','r+')
delete_time.truncate(0)
delete_time.close()

def alarmRing(time):
    time_to_set = str(time)
    time_now = time_to_set.replace('jarvis','')
    time_now = time_now.replace('set alarm for ','')
    time_now = time_now.replace('set ','')
    time_now = time_now.replace('alarm ','')
    time_now = time_now.replace(' and ',':')

    alarm_time = str(time_now)
    while True:
        cTime = datetime.datetime.now().strftime('%H:%M')
        if cTime == alarm_time:
            print('wake up sir, it\'s time to work')
            playsound('C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\Database\\Sounds\\oned.mp3')
        elif cTime > alarm_time:
            break
