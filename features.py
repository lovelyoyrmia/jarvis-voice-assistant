import requests
import geocoder
import os
import wolframalpha
import webbrowser
import pywhatkit 
import wikipedia
from pywikihow import search_wikihow
from geopy.distance import great_circle
from geopy.geocoders import Nominatim


def youtubeSearch(voice_data):
    from main import jarvisSpeak
    results = 'https://www.youtube.com/results?search_query?=' + voice_data

    webbrowser.open(results)

    jarvisSpeak('here is what i found for you sir')

    pywhatkit.playonyt(voice_data)

    jarvisSpeak('this may also help you sir')

def wikipediaSearch(voice_data):
    voice_data = voice_data.replace('wikipedia','')
    from main import jarvisSpeak
    jarvisSpeak('searching wikipedia..')
    results = wikipedia.summary(voice_data, sentences = 2)
    print(str(results))
    jarvisSpeak('according to wikipedia ' + str(results))

def googleSearch(term):
    from main import jarvisSpeak
    voice_data = term.replace('jarvis','')
    voice_data = voice_data.replace('what is','')
    voice_data = voice_data.replace('how to','')
    voice_data = voice_data.replace('who is','')
    voice_data = voice_data.replace(' ','')
    voice_data = voice_data.replace('what do you mean by','')
    writeab = str(voice_data)
    opendata = open('C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\Data.txt','a')
    opendata.write(writeab)
    opendata.close()

    Voice_data = str(term)
    pywhatkit.search(Voice_data) 
    if 'how to' in Voice_data:
        max_result = 1
        how_to_func = search_wikihow(query=Voice_data,max_results=max_result)
        assert len(how_to_func)==1
        how_to_func[0].print()
        jarvisSpeak(how_to_func[0].summary) 
    else:
        results = wikipedia.summary(Voice_data, sentences = 2)
        jarvisSpeak(f'according to google : {results}')

def myLocation():
    from main import jarvisSpeak
    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    longitude = geo_d['longitude']

    latitude = geo_d['latitude'] 

    jarvisSpeak(f'sir, you are now in {state} {country} with longitude {longitude} and latitude {latitude}')

def googleMaps(place):
    from main import jarvisSpeak
    url_place = 'https://google.nl/maps/place/' + place

    user_agent = 'myGeocoder'

    geolocator = Nominatim(user_agent=user_agent)

    location = geolocator.geocode(place, addressdetails=True)

    target_lation = location.latitude , location.longitude

    location = location.raw['address']

    target = {'city' : location.get('city',''),
              'postcode' : location.get('postcode',''),
              'country' : location.get('country',''),
              }
    current_location = geocoder.ip('me')

    current_lation = current_location.latlng

    distance = str(great_circle(current_lation,target_lation))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)
    webbrowser.open(url_place)

    jarvisSpeak(str(target))
    jarvisSpeak(f'sir , {place} is {distance} kilometre away from your location')
    jarvisSpeak(f'do you want to go to{place} sir?')

def alarmSet(query):
    timeNow = open('C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\Data.txt','a')
    timeNow.write(query)
    timeNow.close()
    os.startfile('C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\Database\\Extra\\alarm.py')

def wolfRam(query):
    from main import jarvisSpeak
    api_key = 'PUGTVE-UGAUTTV3L2'

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        print(answer)
        jarvisSpeak(answer)
        return answer
    except:
        jarvisSpeak('an string value is not answerable')

def calculator(query):
    from main import jarvisSpeak
    voice_data = str(query)

    voice_data = voice_data.replace('jarvis','')
    voice_data = voice_data.replace('multiply','*')
    voice_data = voice_data.replace('plus','+')
    voice_data = voice_data.replace('minus','-')
    voice_data = voice_data.replace('plus','+')
    voice_data = voice_data.replace('into','*')

    final = str(voice_data)
    try:
        # sleep(2)
        results = wolfRam(final)
        jarvisSpeak(f'{results}')
    except:
        jarvisSpeak('a string value is not answerable')

def temperature(query):
    from main import jarvisSpeak

    voice_data = str(query)

    voice_data = voice_data.replace('jarvis ','')

    voice_data = voice_data.replace('in','')

    voice_data = voice_data.replace('what is the ','')

    voice_data = voice_data.replace('temperature ','')

    Voice_data = str(voice_data)

    if 'outside' in Voice_data:
        var1 = 'temperature in jakarta'

        answer = wolfRam(var1)

        jarvisSpeak(f'{var1} is {answer}')

    else:

        var2 = 'temperature in ' + Voice_data

        answer = wolfRam(var2)

        jarvisSpeak(f'{var2} is {answer}')

def dateConverter(query):
    date = query.replace(' and ','-')
    date = date.replace(' and ','-')
    date = date.replace('and','-')
    date = date.replace('and','-')
    date = date.replace(' ','-')

    return date

