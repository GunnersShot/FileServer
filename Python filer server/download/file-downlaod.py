from flask import Flask, send_file, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_file():
    filename = request.form['filename']
    # Provide the path to the file you want to download
    file_path = '/var/www/html/downloads/' + filename
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
