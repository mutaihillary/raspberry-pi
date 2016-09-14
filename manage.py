from flask_script import Manager,commands
from flask_migrate import Migrate, MigrateCommand
from run import app
from models import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def init_db():
    with app.test_request_context():
        from models import db
        db.engine.echo = True
        db.metadata.bind = db.engine
        db.metadata.create_all(checkfirst=True)
        #db.create_all(checkfirst=True)

if __name__ == "__main__":
    manager.run()

"""
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from flask_migrate import Migrate

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)


    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(128))
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()"""""