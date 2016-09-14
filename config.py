from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///raspberry.db'
app.config['SECRET_KEY'] = 'really good stuff'