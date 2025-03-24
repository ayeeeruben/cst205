from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)

bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
    s1 = '<p> Ruben : LOL \n</p>'
    s2 = '<p> Alex : wth \n </p>'
    return s1 + s2

@app.route('/ruben')
def temp():
    return render_template('myfirstTemplate.html')

