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
  
  # HOME AWAL
  from app_rabs.home import app_home as home
  app.register_blueprint(home)
  
  # FORM SURVEY
  from app_rabs.form.survey import app_survey as survey
  app.register_blueprint(survey)

  # FORM SURVEY
  from app_rabs.form.rab import app_rab as rab
  app.register_blueprint(rab)
    
  return app 