# creating a basic flask app regarding the personal blogs

# creating basic functionality first which include a home page and about page
from flask import Flask, render_template,request
from models import db, BlogPost
from views import home,post,create_post,about
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
# creating a decorator for the hone page mentioned in views.py
app.route('/')(home)

# creating a decorator for the about page mentioned in views.py
app.route('/about')(about)

# creating a decorator for the view blog function mentioned in views.py
app.route('/post/<post_title>')(post)

#creating a decorator for the create_post function mentioned in views.py
app.route('/create_post',methods=['GET', 'POST'])(create_post)

if __name__ == '__main__':
    app.run(debug=True)
