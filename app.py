import os
import config
from flask import Flask
from models.base_model import db
from flask_wtf.csrf import CSRFProtect

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'book_web') # To check where this appears

app = Flask("BOOK", root_path=web_dir)

csrf = CSRFProtect(app) # for web app in flask

if os.getenv('FLASK_ENV')=='production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

@app.before_request
def before_request():
    db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.closer())
    return exc