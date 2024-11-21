from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@tp1_backend_1:5432/postgres"
db = SQLAlchemy(app)

from models import Book

@app.route("/")
def home():
    books = Book.query.all()
    return render_template("home.html", books=books)
