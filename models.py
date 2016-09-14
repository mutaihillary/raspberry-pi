from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, Boolean, Unicode, Date
from sqlalchemy.orm import relationship
from run import app

db = SQLAlchemy(app)


class User(db.Model):
    id = Column('id',Integer, primary_key=True)
    email = Column('email', string)
    password = Column('password', String)

    def __repr__(self):
        return "<id: %r,email: %r, password: %r>" % (self.id, self.email, self.password)

