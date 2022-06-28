# add views (endpoints) 
from flask import Blueprint

app_jsa = Blueprint('app_jsa', __name__, template_folder='templates', static_folder='static')

from app_rabs.form.jsa import view_jsa