import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:tvKklZfjAwImjUarIHxALIpLIbkvseVO@postgres.railway.internal:5432/railwaytvKklZfjAwImjUarIHxALIpLIbkvseVO"
