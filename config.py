import os
import urllib
basedir = os.path.abspath(os.path.dirname(__file__))
params = urllib.parse.quote_plus(os.environ['DATABASE_URL'])


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'sdfsSAD3asfsfd2345rvSD223CC@F_sDFfSFbSD'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    CORS_ENABLED = True
    JWT_SECRET_KEY = os.environ['JWTSECRET']
    PROPAGATE_EXCEPTIONS = True
    PROPAGATE_EXCEPTIONS = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


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
