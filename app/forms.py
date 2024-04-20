from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password_hash = PasswordField("Password", validators=[DataRequired()])
    education_text = StringField("Education text", validators=[DataRequired()])
    education_level = StringField("Education level", validators=[DataRequired()])
    experience_text = StringField("Experience text", validators=[DataRequired()])
    experience_years = StringField("Experience years", validators=[DataRequired()])
    technologies_text = StringField("Technologies text", validators=[DataRequired()])
    soft_skills_text = StringField("Soft skills text", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
