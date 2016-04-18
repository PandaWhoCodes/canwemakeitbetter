import os

#Have to really learn this properly once deployed on the web cause its just copied from some default flask application

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'mnr1DloWvx9VJC3CJ-hLI2zgSx'
    SQLALCHEMY_DATABASE_URI = os.environ['postgres://wfgbweioifdejs:mnr1DloWvx9VJC3CJ-hLI2zgSx@ec2-79-125-126-192.eu-west-1.compute.amazonaws.com:5432/d98fdmm7p34k7d']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
