
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from processing import do_calculation

app = Flask(__name__)
add.config["DEBUG"] = True
@app.route('/')
def hello_world():
    return 'Jenny testing'

