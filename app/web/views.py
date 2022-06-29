from web import app
from . import google_utils
from flask import render_template, request


@app.route('/')
def index():
    values = {'name' : 'yuta'}
    return render_template('index.html', data=values)

@app.route('/', methods=['POST'])
def post():
    word = request.form.get('word')
    urls = google_utils.get_images_url(word)
    print(word)
    return render_template('result.html',
      data = urls)