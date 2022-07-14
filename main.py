from flask import Flask, render_template, redirect, url_for, flash, request
from forms import EnquiryForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
import os
from datetime import date

# Run Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "MySecretKey")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/photography')
def photography():
    return render_template("photography.html")


@app.route('/enquiries')
def enquiries():
    return render_template("enquiries.html")


if __name__ == "__main__":
    app.run()