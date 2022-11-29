from app import site
from flask import render_template 

@site.route('/')
@site.route('/home')
def index():
    return render_template('index.html')

@site.route('/fav5')
def fav5():
    return render_template('fav5.html', people=site.config["FAVORITE_PEOPLE"])