# contain views to update,add,delete blog post and to view list of blogposts

from flask import render_template,url_for,flash,request,redirect,Blueprint
from website_main import db
from website_main.models import blogposts
from website_main.forms_admin.forms import addform,blog_edits

forms_admin = Blueprint('forms_admin',__name__)

# CREATE
@forms_admin.route('/add',methods=['GET','POST'])
def add():
    form=addform()
    if request.method == 'POST':
        if form.is_submitted():
            print('Form successfully submitted')
        if form.validate_on_submit():
            content = request.form['editordata']
            title = form.title.data
            # pics = form.pics.data
            category = form.category.data

            blog_post = blogposts(title,content,category)
            db.session.add(blog_post)
            db.session.commit()
            flash('Blog Post Created')
        return redirect(url_for('forms_admin.blog_view'))
    return render_template('addform.html',form=form)

# BLOG POST (VIEW) : to  view list of blogpost blog posts
@forms_admin.route('/view')
def blog_view():
#     yet to update the paginate view in html page
    blog = blogposts.query.paginate(1,5, False).items 
    return render_template('blog_post.html',blog=blog)

# BLOG POST (VIEW) to get the data for particular blogpost in update func
@forms_admin.route('/<int:blog_post_id>/edit',methods=['GET','POST'])
def blog_edit(blog_post_id):
    blog_edit = blogposts.query.get_or_404(blog_post_id)
    form = blog_edits()

    if request.method == 'POST':
        if form.validate_on_submit():
            content = request.form['editordata']
            title = form.title.data
            category = form.category.data

            idno = blogposts.query.get_or_404(blog_post_id)
            idno.title=title
            idno.content=content
            idno.category=category
            db.session.commit()

        return(redirect(url_for('forms_admin.blog_view')))

    return render_template('blog_edits.html',title=blog_edit.title,
                            category=blog_edit.category, content=blog_edit.content,form=form)

# DELETE
@forms_admin.route('/<int:blog_post_id>/delete',methods=['GET','POST'])
def delete_post(blog_post_id):

    blog_post = blogposts.query.get_or_404(blog_post_id)
    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('forms_admin.blog_view'))
