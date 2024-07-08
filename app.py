from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    log_content = []
    with open('logs/honeyfile_log.txt', 'r') as log_file:
        log_content = log_file.readlines()
    return render_template('index.html', log_content=log_content)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)
