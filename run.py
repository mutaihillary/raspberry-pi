from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///raspberry.db'
#SQLALCHEMY_MIGRATE_REPO =(raspberry, 'db_repository')
app.config['SECRET_KEY'] = 'really good stuff'


def init_app():
    if __name__ == '__main__':
        app.run(debug=True)


init_app()

