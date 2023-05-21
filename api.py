import requests
import json
import os
import time

params = {
    "count": 1,    
    "client_id": f"VChKUd9T7PmgIYLDbJ4zWtGySM5s4Cq_jsdv-_2jrrQ"
}
    
def search(term, page):
    
    url = "https://api.unsplash.com/search/photos?query={}&page={}" 
    page = page*2-1
    
    request1 = requests.get(url.format(term, page), params=params)
    request2 = requests.get(url.format(term, page+1), params=params)
    
    data = json.loads(request1.text)['results'] + json.loads(request2.text)['results']
    
    # la lista esta compuesta por diccionarios, que tiene las resolucines de las imagenes
    # {"regular": ..., "raw": ..} 
    images = []

    for photo in data:
        images.append((photo['urls']['regular'], photo['urls']['raw']))
        
    return images


# Funcion para descargar las imagenes, dicha funcion almacena las imagenes en la carpeta "temp" 📁
def download_image_from_url(image_url):
    response = requests.get(image_url)
    name = image_url.split('?')[0].split('/')[3] + '.jpg'
    
    filename = os.path.join('static', 'temp', name)
    
    with open(filename, 'wb') as f:
        f.write(response.content)

    return filename
    
    
# funcion para borrar las imagenes en la carpeta temporal
def delete_temp_images(filename):
    formatName = filename.replace("\\", "/")
    
    try:
        time.sleep(10)
        os.remove(formatName)
        print("image deleted ✅")
        return {"message": "image deleted ✅"}
    except IOError:
        print("error to delete image ❌")