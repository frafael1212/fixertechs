from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def hello_world():
    folder_path = "./templates/public/"
    file_open = folder_path / "index.html"
    return render_template(file_open)