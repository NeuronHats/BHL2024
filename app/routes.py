from app import app, db
from app.AI import keywords
from app.models import User, Company, JobPosting
from app.forms import LoginForm, RegistrationForm, EmbedRegistrationForm
import sqlalchemy as sa
from sqlalchemy.orm import joinedload
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
    return render_template("swaper.html", company=company)
    # return render_template('base.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.email == form.email.data))
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
        if not form.company_check.data:
            cv = form.cv.data
            cv_pdf_content = cv.stream.read()
            user = User(
                email=form.email.data,
                is_company=form.company_check.data,
                cv_filename=cv.filename,
                cv_pdf_content=cv_pdf_content,
            )
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
        random_listing = (
            db.session.query(
                JobPosting.title,
                JobPosting.description,
                JobPosting.location,
                JobPosting.salary_range_lower,
                JobPosting.salary_range_upper,
                Company.name.label("company_name"),
                Company.image_b64.label("company_image"),
            )
            .join(Company, JobPosting.company_id == Company.id)
            .where(JobPosting.id == random.randint(1, num_of_listings))
        )
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
        random_listing = (
            db.session.query(
                JobPosting.title,
                JobPosting.description,
                JobPosting.location,
                JobPosting.distance,
                JobPosting.salary_range_lower,
                JobPosting.salary_range_upper,
                Company.name.label("company_name"),
                Company.image_b64.label("company_image"),
            )
            .join(Company, JobPosting.company_id == Company.id)
            .where(JobPosting.id == random.randint(1, num_of_listings))
        )
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

@app.route("/embed_register", methods=["GET", "POST"])
def embed_register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = EmbedRegistrationForm()
    if form.validate_on_submit():
        cv = form.cv.data
        cv_pdf_content=cv.stream.read()
        user = User(email=request.args.get("email"), cv_filename=cv.filename, cv_pdf_content=cv_pdf_content)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("embed_register.html", title="Register", form=form)

@app.route('/express-interest')
def express_interest():
    print(int(request.args.get("userid")))
    print(int(request.args.get("jobid")))
    job = JobPosting.query.get(int(request.args.get("jobid")))
    user = User.query.get(int(request.args.get("userid")))
    
    if not job or not user:
        return jsonify({'error': 'Invalid job or user ID'}), 404

    # Check if the user already expressed interest
    # Add user to job's interested users
    job.interested_users.append(user)
    db.session.commit()

    return jsonify({'message': 'Interest in job offer registered successfully'}), 200


@app.route("/recruiter")
def recruiter():
    job_postings = JobPosting.query.filter_by(company_id=2).options(
        joinedload(JobPosting.interested_users)
    ).all()
    results = []
    for job in job_postings:
        print(job.__dict__)
        job_data = {
            'job_title': job.title,
            'email': job.interested_users.email,
            'cv_filename': job.interested_users.cv_filename,
            'cv_pdf_data': job.interested_users.cv_pdf_content
        }
        results.append(job_data)

    # Return the data as JSON, adjust if you want to render a template
    return jsonify(results)

@app.route("/embed_test")
def embed_test():
    width = 500
    height = 700
    return render_template("embed_test.html", width=width, height=height)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
