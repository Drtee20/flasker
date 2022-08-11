from distutils.command.install_egg_info import safe_name
from flask import Flask, render_template

# creating an instance of Flask

app = Flask(__name__)

# create a route decorator

@app.route('/')

# def index():
#     return '<h1> Hello world </h1>'

#Jinja filters
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags

def index():
     first_name ="John"
     stuff = "this is <strong>Bold Text</strong> "
     favorite_pizza=['pepperoni', 'cheese', 'mushroom', 43]
     return render_template('index.html', first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

#using Ginger templates


@app.route('/user/<name>')
def user(name):
     return render_template('user.html', name=name)

#custom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
     return render_template('404.html'), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
     return render_template('500.html'), 500



if __name__ == '__main__':
     app.run(debug=True) 