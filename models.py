from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, Boolean, Unicode, Date
from sqlalchemy.orm import relationship
from run import app

db = SQLAlchemy(app)


class Login(db.Model):
    id = Column('id', Integer, primary_key=True)
    email = Column('email', unicode)
    password = Column('password', unicode)

    def __repr__(self):
        return "<id: %r,email: %r, password: %r>" % (self.id, self.email, self.password)


class Registration(db.Model):
    id = Column('id', Integer, primary_key=True)
    username = Column('username', unicode)
    email = Column('email', unicode)
    password = Column('password', unicode)

    def __repr__(self):
        return "<id: %r,username: %r, email: %r, password: %r>" % (self.username, self.id, self.email, self.password)

