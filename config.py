'''
Global configurations goes here.
created by: denz 4/27/2017
'''

from utility import key_gen

class Config(object):
    """
    common configuration
    """
    # TODO: think of global configs used across all environments to be placed here. Best Practice etc.


class DevelopmentConfig(Config):
    """
    Development Environment
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production Environment
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

SECRET_KEY = key_gen.generate_password(8)
# TODO need to setup scotch as mysql server and figure out how to install mysql-python
SQL_ALCHEMY_DATABASE_URI = ''
