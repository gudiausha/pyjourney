## App 1 - Website

I have learnt flask webframework in the past few weeks and I have decided to implement whatever I have learnt by creating a personal 
website. Checkout the website_updates.md to see my daily account of the website designing process. The folder strucutre of the repo is as follows:


    website/
     ├── app.py                 #main program
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
          ├── templates/                    #html templates
                 ├── about.html
                 ├── addform.html
                 ├── admin.html
                 ├── article.html
                 ├── base.html
                 ├── blog_edits.html
                 ├── blog_post.html
                 ├── bolist.html
                 ├── books.html
                 ├── contact.html
                 ├── error_pages/
                 │   └── 404.html
                 ├── food.html
                 ├── login.html
                 ├── main.html
                 ├── relist.html
                 ├── thlist.html
                 └── thoughts.html


        
