from flask import Flask, flash, request, redirect
from client import file_consumer

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('NO FILE PART')
            return ''
        audiofile = request.files['file']
        if audiofile:
            file_consumer.handle_audio(audiofile)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
