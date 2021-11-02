import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    RESTX_MASK_SWAGGER = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://dbadmin:dbadmin@satheesh.dev.mysql:3306/db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestConfig(Config):
    DEBUG = True


config_by_name = dict(
    production=ProductionConfig,
    test=TestConfig,
    development=DevelopmentConfig
)
