# will contain blog add form

from flask import Flask, render_template, session, redirect, url_for, session,request
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms import validators
from flask_wtf.file import FileField,FileAllowed
from wtforms.validators import DataRequired
from wtforms import ValidationError




# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class addform(FlaskForm):

    title = StringField('Please enter the title of the blogpost')
    # pics = RadioField('Any pictures?', choices=[('yes','Yes'),('no','No')])
    category = RadioField('Select a Category', choices=[('books','books'),('recipes','recipes'),('thoughts','thoughts')])
    # blog_content = request.form.get('editordata')
    submit = SubmitField('Add')

class blog_edits(FlaskForm):

    title = StringField('Please enter the title of the blogpost')
    # pics = RadioField('Any pictures?', choices=[('yes','Yes'),('no','No')])
    category = RadioField('Select a Category', choices=[('books','books'),('recipes','recipes'),('thoughts','thoughts')])
    # blog_content = request.form.get('editordata')
    submit = SubmitField('Update')

class contactform(FlaskForm):
    name = TextField("Your Name",  [validators.Required("Please enter your name")])
    email = TextField("Enter your Email",  [validators.Required("Please enter your email"),validators.Email("Please enter your email")])
    subject = TextField("Topic of our discussion",  [validators.Required("Please enter the subject")])
    message = TextAreaField("Your message for me goes here",  [validators.Required("Please enter a message")])
    picture = FileField('Do you have any pics to upload', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Send")
