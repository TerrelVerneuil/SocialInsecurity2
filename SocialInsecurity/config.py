import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
# contains application-wide configuration, and is loaded in __init__.py
class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret' # TODO: Use this with wtforms
    DATABASE = 'database.db'
    UPLOAD_PATH = 'app/static/uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "eFWlqSyGBZ0Y1JvqMSHX7HnJvdgBhM1r" 
    app.config['UPLOAD_PATH'] = UPLOAD_PATH
    # Might use this at some point, probably don't want people to upload any file type
