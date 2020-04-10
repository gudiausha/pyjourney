# ../website_main/main/views
from flask import render_template,request,Blueprint

cmain=Blueprint('main',__name__)

@cmain.route('/')
def homepage():
    return(render_template('main.html'))

@cmain.route('/about')
def about():
    return(render_template('about.html'))
