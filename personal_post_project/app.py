# creating a basic flask app regarding the personal blogs

# creating basic functionality first which include a home page and about page
from flask import Flask, render_template,request
from models import db, Blog_Post
from views import home
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

# creating a decorator for the hone page mentioned in views.py
app.route('/')(home)




if __name__ == '__main__':
    app.run(debug=True)






# registering the method in the views.py
# app.route('/posts/<int:post_id>')(view_post)

# #registering my create_post method in the app.py
# @app.route('/create_post', methods=['POST', 'GET'])
# def register_create_post():
#     if request.method == 'POST':
#         return create_post()
    
# #registering my delete_post method in the app.py
# @app.route('/delete_post/<int:post_id>', methods=['POST', 'GET'])
# def register_delete_post(post_id):
#     if request.method == 'POST':
#         return delete_post(post_id)
    


