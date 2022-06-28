from django.shortcuts import render
from flask import render_template, request, redirect, url_for
from app_rabs.form.evaluasi import app_evaluasi
from jinja2 import TemplateNotFound

@app_evaluasi.route('/evaluasi')
def evaluasi():
  return render_template('form/evaluasi/evaluasi-table.html')

@app_evaluasi.route('/add-evaluasi')
def add_evaluasi():
  return render_template('form/evaluasi/evaluasi-form.html')

