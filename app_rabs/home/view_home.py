from flask import render_template, request, redirect, url_for
from app_rabs.home import app_home
from jinja2 import TemplateNotFound

@app_home.route('/')
def route_default():
  return redirect(url_for('app_home.login'))
  
@app_home.route('/login')
def login():
    return render_template('home/sign-in.html')
  
@app_home.route('/home')
def home():
    return render_template('home/index.html')
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


# @app_home.route('/<template>')
# def route_template(template):

#     try:

#         if not template.endswith('.html'):
#             template += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/" + template, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500


# # Helper - Extract current page name from request
# def get_segment(request):

#     try:

#         segment = request.path.split('/')[-1]

#         if segment == '':
#             segment = 'index'

#         return segment

#     except:
#         return None