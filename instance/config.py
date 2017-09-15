import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}


swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Fakerservice",
        "description": "Rest API for the Faker library.",
        # "contact": {
        #     "responsibleOrganization": "ME",
        #     "responsibleDeveloper": "Me",
        #     "email": "me@me.com",
        #     "url": "www.me.com",
        # },
        # "termsOfService": "http://me.com/terms",
        "version": "0.0.1"
    },
    # "host": "fakerservice.com",  # overrides localhost:500
    # "basePath": "/",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ]
}
