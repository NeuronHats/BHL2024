from app import app, db
from app.models import User, Company, JobPosting
from app.forms import LoginForm, RegistrationForm
import sqlalchemy as sa
from flask import jsonify, render_template, redirect, url_for, request, flash
from flask_login import current_user, logout_user, login_user

import random


@app.route("/")
def index():
    company = {
        "img": "company_logo.png",
        "name": "Example Company",
        "position": "Software Engineer",
        "experience": "5 years",
        "education": "Bachelor of Science in Computer Science",
        "salary": "$100,000",
        "city": "San Francisco",
    }
    return render_template("swiping-card.html", company=company)
    # return render_template('base.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.email == form.email.data))
        if user is None or not user.check_password(form.password_hash.data):
            flash("Invalid email or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, is_company=form.company_check.data)
        user.set_password(form.password_hash.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/check")
def check():
    if current_user.is_authenticated:
        return "authed"
    return "not authed"

# DOESNT WORK
@app.route("/embed_json")
def embed_json():
    listings = []
    num_of_listings = db.session.query(JobPosting).count()
    for i in range(10):
        random_listing = db.session.scalar(
            sa.select(JobPosting).where(JobPosting.id == random.randint(1, num_of_listings))
        )
        listings.append(random_listing)
    return jsonify(listings)

@app.route("/embed")
def embed():
    listings = []
    num_of_listings = db.session.query(JobPosting).count()
    for i in range(10):
        random_listing = db.session.scalar(
            sa.select(JobPosting).where(JobPosting.id == random.randint(1, num_of_listings))
        )
        listings.append(random_listing)
    print(listings)
    return render_template("embed.html", listings=listings)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
