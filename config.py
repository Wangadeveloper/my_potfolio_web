import os

class Config:
    SECRET_KEY = "mr powa application"

    #MAIL SETTINGS (GMAIL EXAMPLE)
    # MAIL_SERVER = "smtp.gmail.com"
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True

    # MAIL_USERNAME = "peterwanga326@gmail.com"
    # MAIL_PASSWORD = "@Powa1856"

    MAIL_DEFAULT_SENDER = ("Portfolio Website", "peterwanga326@gmail.com")
    # MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
