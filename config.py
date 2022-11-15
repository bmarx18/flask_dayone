import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
    Sets variable for the flask app. 
    Using environment variable where available.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'While I live -- And until I die -- I am an Avenger!'

