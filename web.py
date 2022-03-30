from flask import Flask

import render


app = Flask(__name__)

@app.route("/")
def index():
    return render.main()
