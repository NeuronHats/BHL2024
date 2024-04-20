import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from typing import Optional
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    firstname: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    lastname: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    education_text: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    education_level: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    experience_text: so.Mapped[Optional[str]] = so.mapped_column(sa.String(512))
    experience_years: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    technologies_text: so.Mapped[Optional[str]] = so.mapped_column(sa.String(512))
    soft_skills_text: so.Mapped[Optional[str]] = so.mapped_column(sa.String(512))
    cv_filename: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    cv_pdf_content: so.Mapped[Optional[bytes]] = so.mapped_column(sa.LargeBinary)
    profile_picture_bytes: so.Mapped[Optional[bytes]] = so.mapped_column(sa.LargeBinary)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"<User {self.email}>"


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
