## Personal Website

I decided to implement whatever I learnt in the udemy flask course by creating a personal website. This is a single user controlled website. i.e only one person has admin access and only he/she can edit,delete,add and view all the posts. Unlike for a blogging website, here I have decided not to provide the users with a login option. So they have read-only access to the web-pages and the post as well. 

## Getting Started
This repo consists of an overall skeleton of my website.  The installations to be done are:

        - Python :- Python 3.8.0
        - Atom IDE
        - Flask framework :-Flask 1.1.2 :- pip install flask 
        - SQL Alchemy for database setup :- Flask-SQLAlchemy 2.4.1 :- pip install Flask-SQLAlchemy
        - For sharing the posts via social media :- Flask-Share 0.1.1 :- pip install Flask-Share
        - For sending email to the admin when the user posts message in the contact form :-Flask-Mail 0.9.1 :- pip install Flask-Mail
 
 The folder structure along with their descriptions is given below.

    website/
     ├── app.py                 #main program to be run
     └── website_main/          
           ├── __init__.py      # contains configuration details of flask,database,email,share app
           ├── data.sqlite
           ├── models.py        # contains database
           ├── datalist/        # views to list of recipes and books
                 │       ├── __init__.py
                 │       ├── views.py
           ├── error_pages/     # error handling page
                 │       ├── handlers.py
           ├── forms_admin/     
                 │       ├── __init__.py
                 │       ├── forms.py      # contact form, add and edit form for blogposts
                 │       ├── views.py      # views for CRUD ops in database
           ├── main/
                 │       ├── __init__.py
                 │       ├── views.py      # views for homepage & other menus
           ├── static/                     # css and image files
                 |        ├── images/
                 │               ├── about1.jpg
                 │               ├── book.jpg
                 │               ├── food1.jpg
                 │               ├── scar.jpg
                 │               └── thought1.jpg
                 |        ├── styles/
                 │               ├── about.css
                 │               ├── base.css
                 │               ├── books.css
                 |               ├── contact.css
                 │               ├── food.css
                 │               ├── main.css
                 |               ├── relist.css
                 │               └── thoughts.css
          ├── templates/                    #html templates for displaying the respective pages.
                 |        ├── about.html
                 |        ├── addform.html
                 |        ├── admin.html
                 |        ├── article.html
                 |        ├── base.html
                 |        ├── blog_edits.html
                 |        ├── blog_post.html
                 |        ├── bolist.html
                 |        ├── books.html
                 |        ├── contact.html
                 |        ├── error_pages/
                 │              └── 404.html
                 |        ├── food.html
                 |        ├── login.html
                 |        ├── main.html
                 |        ├── relist.html
                 |        ├── thlist.html
                 |        └── thoughts.html

## Deployment 
The application can be run in the local environment by executing the below statement. It is hosted on https://127.0.0.1:5000

        python app.py


        
