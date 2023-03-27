from flask import Flask, render_template, request, send_from_directory, redirect, send_file
from api import search, download_image_from_url

app = Flask(__name__, template_folder='templates')

@app.route('/', methods = ['GET', 'POST'])
def home():
    #get method here
    if request.method == 'GET':
        return render_template('index.html')
       

@app.route('/search', methods = ['GET'])
def getImages():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    result = search(query, page)
    return render_template('index.html', result=result, query=query, page=page)
  
    
@app.route('/download', methods = ['GET'])
def download():
    fileurl = request.args.get('imageUrl')
    image = download_image_from_url(fileurl)
    return send_file(image, as_attachment=True) 

    
@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)