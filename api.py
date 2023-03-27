import requests
import json
import os
import random

params = {
    "count": 1,    
    "client_id": f"VChKUd9T7PmgIYLDbJ4zWtGySM5s4Cq_jsdv-_2jrrQ"
}
    
def search(term, page):
    url = f"https://api.unsplash.com/search/photos?query={term}&&page={page}"
    request = requests.get(url, params=params)

    data = json.loads(request.text)['results']

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
    