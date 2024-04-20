import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from typing import Optional
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
user_interests = sa.Table(
    "user_interests",
    db.metadata,
    sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id"), primary_key=True),
    sa.Column(
        "job_posting_id", sa.Integer, sa.ForeignKey("job_posting.id"), primary_key=True
    ),
)


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    is_company: so.Mapped[bool] = so.mapped_column(sa.Boolean, nullable=True)
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


class Company(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[Optional[str]] = so.mapped_column(sa.String(128))
    image_b64: so.Mapped[str] = so.mapped_column(sa.String(100000))
    city: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    address: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    description: so.Mapped[Optional[str]] = so.mapped_column(sa.String(512))
    company_size_lower: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    company_size_higher: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    # Relationship to job postings
    job_postings: so.Mapped[list] = so.relationship(
        "JobPosting", back_populates="company", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Company {self.name}>"

class JobPosting(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(120), nullable=False)
    description: so.Mapped[str] = so.mapped_column(sa.String(1024), default="")
    location: so.Mapped[str] = so.mapped_column(sa.String(256))
    salary_range_lower: so.Mapped[int] = so.mapped_column(sa.Integer)
    salary_range_upper: so.Mapped[int] = so.mapped_column(sa.Integer)
    distance: so.Mapped[str] = so.mapped_column(sa.String(64))
    company_id: so.Mapped[int] = so.mapped_column(
        sa.Integer, sa.ForeignKey("company.id")
    )
    company: so.Mapped[Company] = so.relationship(
        "Company", back_populates="job_postings"
    )

    # Relationship to users interested in the job posting
    interested_users: so.Mapped[list] = so.relationship(
        "User", secondary=user_interests, backref=so.backref("interested_job_postings")
    )


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
