# contains forms to add and update blog posts by admin.
# contains the contact form which is called on food,books and thoughts pages.

from flask import Flask, render_template, session, redirect, url_for, session,request
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms import validators
from flask_wtf.file import FileField,FileAllowed
from wtforms.validators import DataRequired
from wtforms import ValidationError

# form to add a post
class addform(FlaskForm):
    title = StringField('Please enter the title of the blogpost')
    category = RadioField('Select a Category', choices=[('books','books'),('recipes','recipes'),('thoughts','thoughts')]
    submit = SubmitField('Add')

# displays form to edit post                          
class blog_edits(FlaskForm):
    title = StringField('Please enter the title of the blogpost')
    category = RadioField('Select a Category', choices=[('books','books'),('recipes','recipes'),('thoughts','thoughts')])
    submit = SubmitField('Update')

# displays contact form when the reader clicks on link in respective webpages                       
class contactform(FlaskForm):
    name = TextField("Your Name",  [validators.Required("Please enter your name")])
    email = TextField("Enter your Email",  [validators.Required("Please enter your email"),validators.Email("Please enter your email")])
    subject = TextField("Topic of our discussion",  [validators.Required("Please enter the subject")])
    message = TextAreaField("Your message for me goes here",  [validators.Required("Please enter a message")])
    picture = FileField('Do you have any pics to upload', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Send")
