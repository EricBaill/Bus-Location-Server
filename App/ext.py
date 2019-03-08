# -*- coding: utf-8 -*-

from flask_migrate import Migrate
from flask_session import Session
from App.models import db

def init_ext(app):
    Session(app=app)
    db.init_app(app=app)
    migrate = Migrate()
    migrate.init_app(app=app,db=db)




