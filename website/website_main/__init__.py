# ../website_main/init
# hold organizational logic like connecting models and variou blueprints

# set up application
from flask import Flask

app = Flask(__name__)

from website_main.main.views import cmain
from website_main.error_pages.handlers import error_pages

app.register_blueprint(cmain)
app.register_blueprint(error_pages)
