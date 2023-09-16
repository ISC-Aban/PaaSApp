import os
import sys
import socket

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
     html = '''
    <body style="background-color: black;">

    
        <h1 style="color: white;">aaaaa finalment</h1>
        <img src="https://media.discordapp.net/attachments/305058665361309696/1152639559818035230/image.png?width=253&height=236">
    </body>
    '''
    return app.make_response(html)
