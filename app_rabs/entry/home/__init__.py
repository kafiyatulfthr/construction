# add views (endpoints) 
from flask import Blueprint

app_home = Blueprint('app_home', __name__, template_folder='templates', static_folder='static')

from app_rabs.entry.home import views_home