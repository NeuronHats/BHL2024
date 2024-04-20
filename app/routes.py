from app import app, db
import sqlalchemy as sa
from flask import render_template, redirect, url_for, request


@app.route('/')
def index():
    return render_template('swiping-card.html')
