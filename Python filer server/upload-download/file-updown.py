from flask import Flask, render_template, request, redirect, url_for, session
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'Helloworld'

UPLOAD_DIRECTORY = 'UploadedFiles/'
DOWNLOAD_DIRECTORY= '/var/www/html/downloads/'

USERNAME = 'admin'
PASSWORD_HASH = generate_password_hash('Login@2023')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    file.save(file_path)
    return redirect(url_for('upload_success'))

@app.route('/upload-success')
def upload_success():
    return render_template('upload_success.html')

@app.route('/view-uploads', methods=['GET', 'POST'])
def view_uploads():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and check_password_hash(PASSWORD_HASH, password):
            file_list = os.listdir(UPLOAD_DIRECTORY)
            return render_template('view_uploads.html', file_list=file_list)
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and check_password_hash(PASSWORD_HASH, password):
            session['username'] = username
            return redirect(url_for('view_uploads'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login.html')


@app.route('/view-downloads')
def view_downloads():
    global file_list
    file_list = get_file_list()
    return render_template('index.html', show_file_list=True, file_list=file_list)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = DOWNLOAD_DIRECTORY + '/' + filename
    return send_file(file_path, as_attachment=True)

def get_file_list():
    file_list = []
    for file_name in os.listdir(DOWNLOAD_DIRECTORY):
        if os.path.isfile(os.path.join(DOWNLOAD_DIRECTORY, file_name)):
            file_list.append(file_name)
    return file_list


if __name__ == '__main__':
    app.run(debug=True)
