"""
Global configurations goes here.
created by: denz 4/27/2017
"""


class Config(object):
    """
    common configuration
    """


class DevelopmentConfig(Config):
    """
    Development Environment
    """
    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production Environment
    """
    FLASK_DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
