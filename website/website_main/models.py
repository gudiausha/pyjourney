# don't know if it will be needed for me
# this is to hold my 3 tables:books,recipes,randoms
from datetime import datetime
from website_main import db

class blogposts(db.Model):
    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    # pics = db.Column(db.String(100))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    category = db.Column(db.String(100))
    # will be adding image as well

    def __init__(self, title,content,category):
        self.title = title
        # self.pics = pics
        self.content = content
        self.category = category


    def __repr__(self):
        return (f"Post ID: {self.id} -- Date: {self.date} --- Title: {self.title} --- Content: {self.content} ---Category: {self.category}")




# class books():
#     pass
#
# class randoms():
#     pass
