from flask import render_template,redirect,url_for
from . import main
from .forms import CommentForm
from ..models import Comment
Comment= comment.Comment
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)

@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = CommentForm()
    movie = get_pitch(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Comment(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)