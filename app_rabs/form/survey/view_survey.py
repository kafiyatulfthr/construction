from django.shortcuts import render
from flask import render_template, request, redirect, url_for
from app_rabs.form.survey import app_survey
from jinja2 import TemplateNotFound


@app_survey.route('/survey')
def survey():
  return render_template('form/survey/survey-table.html')

@app_survey.route('/add-survey')
def add_survey():
  return render_template('form/survey/survey-form.html')