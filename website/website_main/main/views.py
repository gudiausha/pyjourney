# ../website_main/main/views
from flask import render_template,request,Blueprint

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
