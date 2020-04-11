"""This module handles the routes related to post"""

from blog import db
from flask import render_template, url_for, Blueprint, request, redirect, flash
from blog.models import Post, Comment
from blog.posts.forms import PostForm, CommentForm
from flask_login import login_required
from slugify import slugify
import bleach


posts = Blueprint('posts', __name__)

@posts.route("/post", methods=['GET', 'POST'])
@login_required
def post():
    #this function adds posts to the database
    post = Post.query.all()
    form = PostForm()
    if form.validate_on_submit():
        l = form.title.data
        s = l.lower()
        posts = Post(title=form.title.data, subtitle=form.subtitle.data, link=form.link.data, author=form.author.data, article=form.article.data, slug=slugify(s))
        db.session.add(posts)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('addpost.html', form=form, title='Add Post', legend="Add Post", post=post, directive='noindex')

@posts.route('/posts/<slug>', methods=['GET', 'POST'])  
def article(slug):
    #this route allows the user to visit a page that contains a specific post, and contols the addition of comments  
    posts = Post.query.filter_by(slug=slug).first_or_404()
    post = Post.query.all() 
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(name=bleach.clean(form.name.data), website=bleach.clean(form.website.data), content=bleach.clean(form.content.data), post_id=posts.id)
        db.session.add(comment)
        db.session.commit()
        flash('Hi, thanks for your letting us know your thought! We have just received your comment and it has been submitted to our moderators for review.','success')
        return redirect(url_for('main.home'))
    return render_template('article.html', posts=posts, form=form, title=posts.title, post=post)  
   

@posts.route('/posts/<slug>/update', methods=['GET', 'POST'])  
@login_required
def update_post(slug):
    #This function handles post updates
    posts = Post.query.filter_by(slug=slug).first_or_404()
    post = Post.query.all()
    form = PostForm()

    if form.validate_on_submit():
        posts.title = form.title.data 
        posts.subtitle = form.subtitle.data
        posts.link = form.link.data
        posts.author = form.author.data
        posts.article = form.article.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        form.title.data = posts.title
        form.subtitle.data = posts.subtitle
        form.link.data = posts.link
        form.author.data = posts.author
        form.article.data = posts.article
        
    return render_template('addpost.html', form=form, title='Update Post', legend="Update Post", post=post)