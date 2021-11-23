from app import init_app
from db import db
from flask_sqlalchemy import SQLAlchemy

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()