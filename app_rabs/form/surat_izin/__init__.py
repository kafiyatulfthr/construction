# add views (endpoints) 
from flask import Blueprint

app_surat_izin = Blueprint('app_surat_izin', __name__, template_folder='templates', static_folder='static')

from app_rabs.form.surat_izin import view_surat_izin