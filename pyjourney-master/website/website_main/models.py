# holds the table called blogposts which stores the data
from datetime import datetime
from website_main import db

class blogposts(db.Model):
    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    category = db.Column(db.String(100))
    

    def __init__(self, title,content,category):
        self.title = title
        self.content = content
        self.category = category


    def __repr__(self):
        return (f"Post ID: {self.id} -- Date: {self.date} --- Title: {self.title} --- Content: {self.content} ---Category: {self.category}")




