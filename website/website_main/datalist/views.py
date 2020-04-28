from flask import render_template,url_for,flash,request,redirect,Blueprint,flash
from website_main import db
from website_main.models import blogposts
from website_main.forms_admin.forms import contactform
from flask_mail import Message, Mail
from website_main import mail

datalist = Blueprint('datalist',__name__)

@datalist.route('/relist')
def recipe_list():
    re = blogposts.query.filter_by(category='recipes').all()
    # print(re)
    if len(re)>0:
        return render_template("relist.html",re=re)
    else:
        return render_template("404.html")

@datalist.route('/bolist')
def books_list():
    bo = blogposts.query.filter_by(category='books').all()
    # print(bo)
    if len(bo)>0:
        return render_template("bolist.html",bo=bo)
    else:
        return render_template("404.html")

@datalist.route('/thlist')
def thoughts_list():
    th = blogposts.query.filter_by(category='thoughts').all()
    # print(th)
    if len(th)>0:
        return render_template("thlist.html",th=th)
    else:
        return render_template("404.html")

@datalist.route('/<int:id>')
def article(id):
    article = blogposts.query.get_or_404(id)
    return render_template('article.html',title=article.title,
                            date=article.date,post=article,content=article.content)

@datalist.route('/contact',methods=['GET', 'POST'])
def contact():
    form = contactform()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='gudiawebsite@gmail.com', recipients=['gudiawebsite@gmail.com'])
            msg.body = """
                        From: %s <%s>
                        %s
                        """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html',success=True)

    elif request.method == 'GET':
        return render_template('contact.html', form=form)
