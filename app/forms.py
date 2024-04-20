from flask_wtf import FlaskForm
from app import db
from app.models import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FieldList
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
    submit = SubmitField("Register")

    def validate_email(self, email):
        email = db.session.scalar(sa.select(User).where(User.email == email.data))
        if email is not None:
            raise ValidationError("Please use a different email address.")


class UserInfoForm(FlaskForm):
    firstname = StringField("First name", validators=[DataRequired()])
    lastname = StringField("Last name", validators=[DataRequired()])
    education_text = FieldList("Education", validators=[DataRequired()])