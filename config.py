import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
    TEMPLATES_AUTO_RELOAD = True
    # SQLALCHEMY_DATABASE_URI = "sqlite+libsql://bhl2024-bberni.turso.io/?authToken=eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3MTM2MTY3OTQsImlkIjoiYjllZTU2YTgtYzkzMi00NTg1LWFmMzEtMjZlMTk2ZTBkZjI3In0.fBF-4dtac4bZv2SU_urIvE12Jx22uju9Jd3-fKSIuD8JjLAdAWeMxYWgZT6UJirfBtqp5STbyPcQFMeWYNOiDw&secure=true"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
