import requests
import json

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
        
        images.append({
            "quality": {
                "thumb": photo['urls']['thumb'],
                "small": photo['urls']['small'],                
                "regular": photo['urls']['regular'],
                "full": photo['urls']['full'],
                "raw": photo['urls']['raw']
            }
            })
        
    return images