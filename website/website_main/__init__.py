# ../website_main/init
# hold organizational logic like connecting models and variou blueprints

# set up application
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_share import Share
from flask_mail import Message, Mail

app = Flask(__name__)
# Configure a secret SECRET_KEY
app.config['SECRET_KEY'] = '@@@@@'
############################
### DATABASE SETUP ##########
########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

@app.before_first_request
def create_tables():
    db.create_all()

######################################
######enanbling share feature########
share = Share(app)

#####################################
#####################################
#########Contact form feature########
#####################################

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TSL"] = False
app.config["MAIL_USERNAME"] = 'sender@example.com'
app.config["MAIL_PASSWORD"] = 'sender-password'

mail = Mail(app)

# here website_main(name of folder);main(name of folder inside website_main);views.py file;cmain(blueprint obj in views file)
from website_main.main.views import cmain
from website_main.error_pages.handlers import error_pages
from website_main.forms_admin.views import forms_admin
from website_main.datalist.views import datalist

app.register_blueprint(cmain)
app.register_blueprint(error_pages)
app.register_blueprint(forms_admin)
app.register_blueprint(datalist)
