import requests
import json
import os
import random

params = {
    "count": 1,    
    "client_id": f"VChKUd9T7PmgIYLDbJ4zWtGySM5s4Cq_jsdv-_2jrrQ"
}
    
def search(term, page):
    
    page = page*2-1
    
    
    url1 = f"https://api.unsplash.com/search/photos?query={term}&page={page}"
    request1 = requests.get(url1, params=params)

    url2 = f"https://api.unsplash.com/search/photos?query={term}&page={page+1}"
    request2 = requests.get(url2, params=params)
    
    data = json.loads(request1.text)['results'] + json.loads(request2.text)['results']
    
    images = []

    for photo in data:
        images.append((photo['urls']['regular'], photo['urls']['raw']))
        
    return images


def download_image_from_url(image_url):
    response = requests.get(image_url)
    name = image_url.split('?')[0].split('/')[3] + '.jpg'
    
    filename = os.path.join('static', 'temp', name)
    
    with open(filename, 'wb') as f:
        f.write(response.content)

    return filename
    