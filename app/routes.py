from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm
import sqlalchemy as sa
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, logout_user, login_user


@app.route('/')
def index():
    company = {
        'img': 'company_logo.png',
        'name': 'Example Company',
        'position': 'Software Engineer',
        'experience': '5 years',
        'education': 'Bachelor of Science in Computer Science',
        'salary': '$100,000',
        'city': 'San Francisco'
    }
    # return render_template('swiping-card.html', company=company)
    return render_template('base.html')


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


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
