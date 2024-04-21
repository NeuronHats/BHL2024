from app import app, db
from app.AI import keywords
from app.models import User, Company, JobPosting, Cache
from app.forms import LoginForm, RegistrationForm, EmbedRegistrationForm
import sqlalchemy as sa
import io
from sqlalchemy.orm import joinedload
from flask import jsonify, render_template, redirect, url_for, request, flash, Response
from flask_login import current_user, logout_user, login_user
from pypdf import PdfReader
import os
import random
import openai

openai.api_key = os.getenv("OPENAI_KEY", "")


@app.route("/")
def index():
    # company = {
    #     "img": "company_logo.png",
    #     "name": "Example Company",
    #     "position": "Software Engineer",
    #     "experience": "5 years",
    #     "education": "Bachelor of Science in Computer Science",
    #     "salary": "$100,000",
    #     "city": "San Francisco",
    # }
    # return render_template("swaper.html", company=company)
    listings = []
    for i in range(1,6):
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
            .where(JobPosting.id == i)
        )
        data = random_listing.all()
        posting = {}
        print(data)
        posting["company"] = data[0][6]
        posting["title"] = data[0][0]
        posting["location"] = data[0][2]
        posting["distance"] = data[0][3]
        posting["lower"] = data[0][4]
        posting["upper"] = data[0][5]
        posting["image"] = data[0][-1]
        posting["mode"] = data[0][1]
        listings.append(posting)
    random.shuffle(listings)
    return render_template("index.html", listings=listings)


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
    for i in range(1,6):
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
            .where(JobPosting.id == i)
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
        posting["mode"] = data[0][1]
        listings.append(posting)
    random.shuffle(listings)
    return render_template("embed.html", listings=listings)


@app.route("/embed_register", methods=["GET", "POST"])
def embed_register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = EmbedRegistrationForm()
    if form.validate_on_submit():
        cv = form.cv.data
        cv_pdf_content = cv.stream.read()
        user = User(
            email=request.args.get("email"),
            cv_filename=cv.filename,
            cv_pdf_content=cv_pdf_content,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("embed_register.html", title="Register", form=form)


@app.route("/express-interest")
def express_interest():
    print(int(request.args.get("userid")))
    print(int(request.args.get("jobid")))
    job = JobPosting.query.get(int(request.args.get("jobid")))
    user = User.query.get(int(request.args.get("userid")))

    if not job or not user:
        return jsonify({"error": "Invalid job or user ID"}), 404

    # Check if the user already expressed interest
    # Add user to job's interested users
    job.interested_users.append(user)
    db.session.commit()

    return jsonify({"message": "Interest in job offer registered successfully"}), 200


@app.route("/recruiter")
def recruiter():
    job_postings = (
        JobPosting.query.filter_by(company_id=2)
        .options(joinedload(JobPosting.interested_users))
        .all()
    )
    results = []
    for job in job_postings:
        job_data = {
            "job_title": job.title,
            "email": job.interested_users.email,
            "cv_filename": job.interested_users.cv_filename,
            "cv_pdf_data": job.interested_users.cv_pdf_content,
            "keywords": job.keywords.split(" "),
            "user_id": job.interested_users.id,
            "job_id": job.id
        }
        pdf_io = io.BytesIO(job_data["cv_pdf_data"])
        cache_hit = db.session.query(Cache.summary).filter_by(user_id=job_data["user_id"], job_id=job_data["job_id"]).first()
        if not cache_hit:
            text = PdfReader(pdf_io).pages[0].extract_text()
            job_data["score"] = keywords.search_keywords(job_data["keywords"], text)
            summary = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"You are given text from the CV of the candidate for the position of {job.title}. Keywords for this position are: {job.keywords}. Summarize it, and based on the content, provide recommendation (of lack there of). Be quite harsh on your judgements, and elaborate on them, but not too much. Your output will server as aid for the recruiter. DO NOT print any markdown. Pay more attention to listed technical skills, not for about me section. Here is text to analyze: {text}"}]
            )
            response = summary.choices[0].message.content
            cache_record = Cache(user_id=job_data["user_id"], job_id=job_data["job_id"], summary=f"{job_data['score']};{response}")
            db.session.add(cache_record)
            db.session.commit()
            job_data["ai_summary"] = response
        else:
            job_data["score"] = float(cache_hit.summary.split(";")[0])
            job_data["ai_summary"] = cache_hit.summary.split(";")[1]

        results.append(job_data)

    # Return the data as JSON, adjust if you want to render a template
    return render_template("recruiter.html", results=results)

@app.route("/download/<filename>")
def download(filename):
    user = User.query.filter_by(cv_filename=filename).first()
    return Response(user.cv_pdf_content, mimetype='application/pdf')

@app.route("/embed_test")
def embed_test():
    width = 500
    height = 900
    return render_template("embed_test.html", width=width, height=height)


@app.route("/applications")
def applications():
    aplications = []
    return render_template("aplications.html", aplications=aplications)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
