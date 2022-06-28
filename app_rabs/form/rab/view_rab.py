from django.shortcuts import render
from flask import render_template, request, redirect, url_for
from app_rabs.form.rab import app_rab
from jinja2 import TemplateNotFound

@app_rab.route('/rab')
def rab():
  return render_template('form/rab/rab-table.html')

@app_rab.route('/add-rab-harian')
def add_rab_harian():
  return render_template('form/rab/rab-form-harian.html')

@app_rab.route('/add-rab-borongan')
def add_rab_borongan():
  return render_template('form/rab/rab-form-borongan.html')