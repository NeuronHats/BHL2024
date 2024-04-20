from flask_wtf import FlaskForm
from app import db
from app.models import User
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    FileField,
    IntegerField,
)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import sqlalchemy as sa


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password_hash = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password_hash = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password_hash")]
    )
    company_check = BooleanField("Recruiter account")
    submit = SubmitField("Register")

    def validate_email(self, email):
        email = db.session.scalar(sa.select(User).where(User.email == email.data))
        if email is not None:
            raise ValidationError("Please use a different email address.")


class NewJobListingForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    localization = StringField("Localization", validators=[DataRequired()])
    lower_bound = IntegerField("Salary lower bound", validators=[DataRequired()])
    higher_bound = IntegerField("Salary higher bound", validators=[DataRequired()])
    submit = SubmitField("Post job listing")


class UserInfoForm(FlaskForm):
    firstname = StringField("First name", validators=[DataRequired()])
    lastname = StringField("Last name", validators=[DataRequired()])
    education_text = StringField("Education")
    experience_years = IntegerField("Work expierience (years)", default=0)
    experience_text = StringField("Education")
    technologies_text = StringField("Technologies")
    soft_skills_text = StringField("Soft Skills")
    cv_file = FileField("Upload your resume: ", validators=[DataRequired()])
    profile_picture_file = FileField("Upload your profile picture (JPG)", validators=[DataRequired()])
