import requests
import os
from PIL import Image

api_key = 'KrsOGOZLgYGcxYVBLZld2U65PevfTyOfbdqy7ggK'

def nasaNews(date):

    from main import jarvisSpeak
    jarvisSpeak('extracting data from nasa')

    url = 'https://api.nasa.gov/planetary/apod?api_key=' + api_key

    params = {'date': str(date)}

    r = requests.get(url,params=params)

    data = r.json()

    info = data['explanation']

    title = data['title']

    image_url = data['url']

    image_r = requests.get(image_url)

    filename = str(date) + '.jpg'

    with open(filename,'wb') as f:
        f.write(image_r.content)
    
    path_1 = 'C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\' + filename
    path_2 = 'C:\\Users\\user\\Documents\\my app\\python_project\\VoiceAssistant\\Database\\NasaDatabase\\' + filename

    os.rename(path_1,path_2)

    image = Image.open(path_2)

    image.show()

    print(info)
    print(title)

    jarvisSpeak(f'title : {title}')
    jarvisSpeak(f'according to nasa: {info}')
    
