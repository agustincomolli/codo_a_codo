from flask import render_template, request
from app import app, db
from app.models import persons


@app.route("/")
def index():
    persons_data = persons.query.all()
    context = {
        "persons": persons_data
    }
    return render_template("index.html", **context)
