# ../website_main/main/views
# basic flask imports
from flask import render_template,request,Blueprint,redirect, url_for,Flask
# database import from __init__.py
from website_main import db
# table(called blogpost)import from models.py
from website_main.models import blogposts

cmain=Blueprint('cmain',__name__)

# routing to homepage
@cmain.route('/')
def homepage():
    return(render_template('main.html'))

# routing to about page
@cmain.route('/about')
def about():
    return(render_template('about.html'))

# routing to food page
@cmain.route('/food')
def food():
    return(render_template('food.html'))

# routing to book page
@cmain.route('/books')
def books():
    return(render_template('books.html'))

# routing to Thoughts page
@cmain.route('/thoughts')
def thoughts():
    return(render_template('thoughts.html'))

# routing to admin page which consists of a form through which we can add,delete,update blogposts
@cmain.route('/admin')
def admin():
    return(render_template('admin.html'))

# routing to login page:basic authentication to view the admin page
@cmain.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != '##########' or request.form['password'] != '########':
            error = 'Invalid Credentials. Please try again.This is only for admin to login'
        else:
            return redirect(url_for('cmain.admin'))
    return render_template('login.html', error=error)

@cmain.route("/logout")
def logout():
    # logout_user()
    return redirect(url_for("cmain.homepage"))
