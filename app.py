from flask import Flask, render_template, request, send_from_directory
from functions.search import search
import os

app = Flask(__name__, template_folder='templates')

download_quality = {
        "thumb": 200,
        "small": 640,
        "regular": 1920,
        "original": "" 
    }

@app.route('/', methods = ['GET'])
def home():
    query = request.args.get('query', 'random')
    page = int(request.args.get('page', 1))
    result = search(query, page)
    return render_template('index.html', result=result, query=query, page=page, quality=download_quality)
       

@app.route('/search', methods = ['GET'])
def getImages():
    query = request.args.get('query', 'random')
    page = int(request.args.get('page', 1))
    result = search(query, page)
    return render_template('index.html', result=result, query=query, page=page, quality=download_quality)
  

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)
