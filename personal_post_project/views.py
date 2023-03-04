from flask import render_template,request,redirect,url_for
from models import db, Blog_Post
from datetime import datetime


def home():
    posts = Blog_Post.query.all()
    return render_template('home.html', posts=posts)

# def create_post():
#     if request.method == 'POST':
#         title = request.form.get('title')
#         content = request.form.get('content')
#         post = Post(title=title, content=content, date_posted=datetime.utcnow())
#         db.session.add(post)
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template('create_post.html')

# # writing a function to delete a post and printing a message success or failure and redirecting to home page
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     db.session.delete(post)
#     db.session.commit()
#     return redirect(url_for('home'))

# # writing a function to update a post and printing a message success or failure and redirecting to home page
# def update_post(post_id):
#     post = Post.query.get_or_404(post_id)
    
#     if request.method == 'POST':
#         post.title = request.form.get('title')
#         post.content = request.form.get('content')
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template('update_post.html', post=post)

