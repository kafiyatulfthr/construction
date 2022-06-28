from flask import Flask
from flask_migrate import Migrate

from config import DevelopmentConfig

from flask_sqlalchemy import SQLAlchemy

from flask_mysqldb import MySQL
import MySQLdb.cursors

# import extensions instance
db = SQLAlchemy()
migrate = Migrate()
mysql = MySQL()
curMysql = MySQLdb.cursors.DictCursor

# instance of migrate flask
migrate = Migrate()

def app_rabs(config=DevelopmentConfig):
  app = Flask(__name__)
  app.config.from_object(config)
  app.config["DEBUG"] = True 
  
  @app.after_request
  def after_request(response):
      response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
      response.headers["Expires"] = 0
      response.headers["Pragma"] = "no-cache"
      return response
  
  app.config['MYSQL_HOST']='localhost'  # dikoneksikan dengan database
  # app.config['MYSQL_HOST']='172.20.140.98'  # dikoneksikan dengan database
  app.config['MYSQL_USER']='root'
  app.config['MYSQL_PASSWORD']='666666'
  # app.config['MYSQL_PASSWORD']=''
  app.config['MYSQL_DB']='kalung_db'

  # initialize extension instances
  mysql.init_app(app)
  mysql.app = app

  # initialize extension instances
  db.init_app(app)
  db.app = app
  
  # migrate initialization
  migrate.init_app(app, db)
  migrate.app = app
  
    
  # ----------register blueprints of applications----------- #
  
  # HOME AWAL
  from app_rabs.authentication.login import app_login_init as login
  app.register_blueprint(login)
  
  # HOME AWAL
  from app_rabs.home import app_home as home
  app.register_blueprint(home)
  
  # FORM SURVEY
  from app_rabs.form.survey import app_survey as survey
  app.register_blueprint(survey)

  # FORM RAB
  from app_rabs.form.rab import app_rab as rab
  app.register_blueprint(rab)
  
  # FORM JSA
  from app_rabs.form.jsa import app_jsa as jsa
  app.register_blueprint(jsa)
  
  # FORM SURAT IZIN
  from app_rabs.form.surat_izin import app_surat_izin as surat_izin
  app.register_blueprint(surat_izin)
    
  # FORM EVALUASI
  from app_rabs.form.evaluasi import app_evaluasi as evaluasi
  app.register_blueprint(evaluasi)
  
  # FORM COMPLETED PROJECT
  from app_rabs.work_board.completed_project import app_completed_project as completed_project
  app.register_blueprint(completed_project)
  
  return app 