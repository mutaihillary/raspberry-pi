from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'really good stuff'


def init_app():
    if __name__ == '__main__':
        app.run(debug=True)
