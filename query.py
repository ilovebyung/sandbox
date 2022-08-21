# pip install python-dateutil
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import sqlite3
import datetime
from sqlalchemy import select
# from datetime import datetime
from dateutil import parser

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Post(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)


# insert
query = Post(name='byung', text='Boston University')
db.session.add(query)
db.session.commit()

# select
found = bool(db.session.query(Post).filter_by(name='byung').first())
print(found)
Post(name='byung', text='Boston University')
db.session.add(query)
db.session.commit()

# update
query = Post.query.filter_by(name='byung').first()
query.text = 'updated'
db.session.commit()

# delete
Post.query.filter_by(name='byung').delete()
db.session.commit()

'''
from ____ import db
db.create_all()
from ____ import TB
db.create_all()
row = TB(name='ilnam')
db.session.add(row)
db.session.commit()
TB.query.all()
TB.query.get_or_404(24)
TB.query.filter_by(name='byung').all()
name = TB.query.get(1)
'''
