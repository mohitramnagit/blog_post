#developing a model for my personal blog

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Blog_Post(db.Model):
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
