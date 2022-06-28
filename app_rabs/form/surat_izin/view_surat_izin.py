from django.shortcuts import render
from flask import render_template, request, redirect, url_for
from app_rabs.form.surat_izin import app_surat_izin
from jinja2 import TemplateNotFound

@app_surat_izin.route('/surat-izin')
def surat_izin():
  return render_template('form/surat_izin/si-table.html')

@app_surat_izin.route('/add-surat-izin')
def add_surat_izin():
  return render_template('form/surat_izin/si-form.html')

