import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False # disabled for api build. Need to enable for flask web build
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProductionConfig(Config):
    DEBUG = False
    ASSETS_DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    ASSETS_DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ASSETS_DEBUG = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    ASSETS_DEBUG = True