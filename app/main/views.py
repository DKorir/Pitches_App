from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)


@main.route('/login',methods=['GET','POST'])
def login():
    return()
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
