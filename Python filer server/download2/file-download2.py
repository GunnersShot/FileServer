from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

DOWNLOAD_DIRECTORY = '/var/www/html/downloads/'
file_list = []

@app.route('/')
def index():
    return render_template('index.html', show_file_list=False)

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
