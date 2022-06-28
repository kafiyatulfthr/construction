# add views (endpoints) 
from flask import Blueprint

app_rab = Blueprint('app_rab', __name__, template_folder='templates', static_folder='static')

from app_rabs.form.rab import view_rab