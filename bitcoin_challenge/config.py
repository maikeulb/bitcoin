import os


class Config(object):

    API_URL = 'https://www.bitmex.com/api/v1/instrument/compositeIndex?symbol=.XBT&filter=%7B%22timestamp.time%22%3A%2210%3A55%3A00%22%2C%22reference%22%3A%22BSTP%22%7D&count=100&reverse=true'

    DEVELOPMENT = False
    TESTING = False
    PRODUCTION = False
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    DEBUG_TB_ENABLED = True


class ProductionConfig(Config):
    PRODUCTION = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
