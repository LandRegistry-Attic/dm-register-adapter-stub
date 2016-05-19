"""
Flask config script for regad_stub.
"""

class Config(object):
    """
    Production Configuration.
    """
    DEBUG = False

class DevelopmentConfig(Config):
    """
    Development Configuration.
    """
    DEBUG = True
