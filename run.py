from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'really good stuff'


def init_app():

    debug = True
    #if __name__ == "__main__":

