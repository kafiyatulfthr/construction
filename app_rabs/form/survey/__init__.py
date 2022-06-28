# add views (endpoints) 
from flask import Blueprint

app_survey = Blueprint('app_survey', __name__, template_folder='templates', static_folder='static')

from app_rabs.form.survey import view_survey