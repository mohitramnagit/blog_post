from flask import render_template,request,redirect,url_for
from models import db, BlogPost
from datetime import datetime

# writing a function for the home page which will have a list of all the blogs
def details():
    posts = BlogPost.query.all()
    return render_template('details.html', posts=posts)

#writing a function for a blog which has been linked to home page using post_name and shows the content of the blog
def post(post_title):
    post = BlogPost.query.filter_by(title=post_title).one()
    return render_template('post.html', post=post)

#writing a function which will take input from a create.html page and write it to the database
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        time=datetime.now()
        post = BlogPost(title=title, content=content, date_posted=time)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('details'))
    return render_template('create_post.html')

# writing a function for the about page which will have a list of all the blogs
def about():
    return render_template('about.html')


