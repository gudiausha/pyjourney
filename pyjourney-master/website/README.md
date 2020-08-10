## Personal Website

I decided to implement whatever I learnt in the udemy flask course by creating a simple personal website. This is a single user controlled website. i.e only one person has admin access and only he/she can edit,delete,add and view all the posts. Unlike for a blogging website, here I have decided not to provide the users with a login option. So they have read-only access to the web-pages and the post as well. 

### Getting Started
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

### Deployment 
The application can be run in the local environment by executing the below statement. It is hosted on https://127.0.0.1:5000

        python app.py

Here are few snapshots of the website after local hosting:

   ![Website Homepage](pyjourney-master/website/website 1.JPG)

   ![Wesite-Books page](pyjourney-master/website/website 2.JPG)

   ![Website-Admin login page](pyjourney-master/website/website 3.JPG)
   
### Lessons Learnt
* <b> Don't complicate</b> the website designing process. First complete the basic design and then start modifying it.
* Make notes as and when possible to keep track of the progress(u can check <a href="pyjourney-master/website/website_updates.md">my journal</a> for reference)
* In terms of technical knowledge,first I learnt the difference between static website and web applications.
* Next is that a web application has client side and server side. Second is about cloud services and more importantly implementing them. I read about google, heroku cloud hosting, tried it to but found them a little difficult. Instead I decided to go with python-anywhere.com its good for a beginner to understand. 
* More importantly I understood how the same code reacts differently in dev as well as prod environment. And how to resolve those issues.Third i learnt the actual meaning of microframework and how python is used for server side logic.
      
### Next Steps
* Implemented multiple routing, but it didn't work out when viewing multiple pages after that. Must look into that. 
        example: 
             
             - tried multiple routing for food.html page:
             - In main->views.py
             
                        @cmain.route('/food')
                        @cmain.route('/food/<int:id>')
                        def food(id=None):
                                if id:
                                     re = blogposts.query(category='food')
                                     render_template('food.html',re=re,success=True)
                                else:
                                     render_template('food.html')
                                     
              - The above changes gave the required result. But the problem occured when clicking other pages after going to /food/1,                   the homepage is displayed. ie.
                        /food/1 -> /food/about -> actual output:about page, output got: homepage
              
                The idea I got to counter this problem is to add various combinations of all posisble routes which i think is not a good                 solution. 
                
* A little more secure approach of admin login maybe using flask security or other options

### References

* Jose Portilla's Udemy course: 'Python and Flask Bootcamp:Create Websites using Flask!'
* In terms of theory explanation and ideas : https://blog.miguelgrinberg.com/ 
* For the wonderful pictures which made my website beautiful: https://unsplash.com/
* While coding I referred to many repos and stackoverflow,but these two repos in particular were in line with my ideas: 
     * https://github.com/ZainQasmi/PyBlog (to get an idea about cloud hosting and article's page)
     * https://github.com/kirankoduru/flask-cms-demo (used this to get an idea of the CRUD operations in database)
     * https://code.tutsplus.com (for the contact form)
     * https://html-css-js.com (emoticon appearance)
     * https://w3schools.com (html,css and bootstrap)
     * https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ (for flask related queries....its an <b><i>awesome</b></i> channel)

On a lighter note don't forget to mention me when you fork this repo. Any suggestions for improving this website are welcome.
