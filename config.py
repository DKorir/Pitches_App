import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY='secret_key'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dominic:12345@localhost/my_pitches'
    DEBUG = True

config_options = {

    'development': DevConfig,
    'production': ProdConfig,

}