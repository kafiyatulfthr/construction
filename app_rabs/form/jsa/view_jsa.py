from django.shortcuts import render
from flask import render_template, request, redirect, url_for
from app_rabs.form.jsa import app_jsa
from jinja2 import TemplateNotFound

@app_jsa.route('/jsa')
def rab():
  return render_template('form/jsa/jsa-table.html')

@app_jsa.route('/add-jsa')
def add_jsa():
  return render_template('form/jsa/jsa-form.html')
