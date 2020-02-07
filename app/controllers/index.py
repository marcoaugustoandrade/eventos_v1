from app import app
from flask import render_template


# A página lista todos os eventos, ordenando pelos mais próximos
@app.route("/")
def home():
    return render_template("index.html")
