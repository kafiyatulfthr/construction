# add views (endpoints) 
from flask import Blueprint

app_evaluasi = Blueprint('app_evaluasi', __name__, template_folder='templates', static_folder='static')

from app_rabs.form.evaluasi import view_evaluasi