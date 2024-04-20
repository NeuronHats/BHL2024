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
    return render_template('swaper.html', company=company)
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

# STILL DOESNT WORK
@app.route("/embed_json")
def embed_json():
    listings = []
    num_of_listings = db.session.query(JobPosting).count()
    for i in range(10):
        random_listing = db.session.query(
        JobPosting.title,
        JobPosting.description,
        JobPosting.location,
        JobPosting.salary_range_lower,
        JobPosting.salary_range_upper,
        Company.name.label('company_name'),
        Company.image_b64.label('company_image')
        ).join(Company, JobPosting.company_id == Company.id).where(JobPosting.id == random.randint(1, num_of_listings))
        data = random_listing.all()
        print(data)
        posting = {}
        posting["company"] = data[0][5]
        posting["title"] = data[0][0]
        posting["lower"] = data[0][3]
        posting["upper"] = data[0][4]
        posting["image"] = data[0][-1]
        listings.append(posting)
    # print(listings)
    return jsonify(listings)

@app.route("/embed")
def embed():
    listings = []
    num_of_listings = db.session.query(JobPosting).count()
    for _ in range(10):
        random_listing = db.session.query(
        JobPosting.title,
        JobPosting.description,
        JobPosting.location,
        JobPosting.distance,
        JobPosting.salary_range_lower,
        JobPosting.salary_range_upper,
        Company.name.label('company_name'),
        Company.image_b64.label('company_image')
        ).join(Company, JobPosting.company_id == Company.id).where(JobPosting.id == random.randint(1, num_of_listings))
        data = random_listing.all()
        posting = {}
        posting["company"] = data[0][6]
        posting["title"] = data[0][0]
        posting["location"] = data[0][2]
        posting["distance"] = data[0][3]
        posting["lower"] = data[0][4]
        posting["upper"] = data[0][5]
        posting["image"] = data[0][-1]
        listings.append(posting)
    return render_template("embed.html", listings=listings)

@app.route("/embed_test")
def embed_test():
    width = 500
    height = 700
    return render_template("embed_test.html", width=width, height=height)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
