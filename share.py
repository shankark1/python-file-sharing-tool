from flask import Flask, send_from_directory
import os

app = Flask(__name__)

SHARED_FOLDER = "shared"

@app.route("/")
def home():

    files = os.listdir(SHARED_FOLDER)

    result = "<h2>Shared Files</h2>"

    for file in files:
        result += f'<a href="/download/{file}">{file}</a><br><br>'

    return result

@app.route("/download/<filename>")
def download_file(filename):

    return send_from_directory(
        SHARED_FOLDER,
        filename,
        as_attachment=True
    )

app.run(host="0.0.0.0", port=5000, debug=True)