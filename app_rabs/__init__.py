from flask import Flask
from flask_migrate import Migrate

from config import DevelopmentConfig

from flask_sqlalchemy import SQLAlchemy

# create an instance of the extension with initializing it
db = SQLAlchemy()

# instance of migrate flask
migrate = Migrate()

def app_rabs(config=DevelopmentConfig):
  app = Flask(__name__)
  app.config.from_object(config)
  
  # initialize extension instances
  db.init_app(app)
  db.app = app
  
  # migrate initialization
  migrate.init_app(app, db)
  migrate.app = app
  
    
  # ----------register blueprints of applications-----------
  
  from app_rabs.entry.home import app_home as home
  app.register_blueprint(home)

  return app 