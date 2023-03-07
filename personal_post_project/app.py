# creating a basic flask app regarding the personal blogs

# creating basic functionality first which include a home page and about page
from flask import Flask, url_for
from models import db, BlogPost
from views import details,post,create_post,about,delete_post
from werkzeug.routing import Rule

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# route for the details page
app.add_url_rule(rule='/details', view_func=details, methods=['GET'])

# route for the about page
app.add_url_rule(rule='/about', view_func=about, methods=['GET'])
app.add_url_rule(rule='/',view_func=about, methods=['GET'])

#route for post page
app.add_url_rule(rule='/post/<post_title>', view_func=post, methods=['GET'])

#route for create_post page
app.add_url_rule(rule='/create_post', view_func=create_post, methods=['GET', 'POST'])

#route for delete_post page
app.add_url_rule(rule='/delete_post/<post_title>', view_func=delete_post, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
