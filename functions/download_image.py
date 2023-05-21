import requests
import os
from urllib.parse import urlparse, parse_qs


def download_image_from_url(image_url):
    
    url = urlparser(image_url)
    
    response = requests.get(url['base'], params=url['params'])

    name = image_url.split('?')[0].split('/')[3] + '.jpg'
    
    filename = os.path.join('static', 'temp', name)

    #urllib.request.urlretrieve(url, name)
    
    with open(filename, 'wb') as f:
          f.write(response.content)

    print(url)
    return filename

    
def urlparser(url):
    parsed_url = urlparse(url)
    
    return {
        "base": parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path,
        "params": parse_qs(parsed_url.query)
    }
    