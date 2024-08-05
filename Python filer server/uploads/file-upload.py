from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_DIRECTORY = 'UploadedFiles/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    file.save(file_path)
    return 'File uploaded successfully.'

if __name__ == '__main__':
    app.run(debug=True)
