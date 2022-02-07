import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY='secret_key'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("tommykiprono.db@gmail.com")
    MAIL_PASSWORD = os.environ.get("T1234567-h")




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