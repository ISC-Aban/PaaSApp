import os
import sys
import socket

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    version = sys.version_info
    res = (
        "<body style='background-color: black;'>"
        "<h1 style='color: white;'>aaaaaa finalmenttt</h1>"
        "<img src='https://media.discordapp.net/attachments/305058665361309696/1152639559818035230/image.png?width=253&height=236'>"
        f"<h2>{os.getenv('ENV')}</h2></br>"
        f"Running Python: {version.major}.{version.minor}.{version.micro}<br>"
        f"Hostname: {socket.gethostname()}"
        " </body>"
    )
    return res

