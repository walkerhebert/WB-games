from flask import Flask, render_template, request, redirect, flash, session
from model import connect_to_db, db
import crud
import json
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "wb-games-key-secret-key"

@app.route("/")
def homepage():
    """View Homepage"""
    
    return render_template("home.html")





if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)