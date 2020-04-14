"""This module handles the routes for the site pages"""

from flask import render_template, url_for, Blueprint, redirect, flash
from blog import db
from blog.models import Post, ContactUs
from blog.main.forms import ContactForm
import bleach

main = Blueprint('main', __name__)


@main.route("/portfolio", methods=['GET', 'POST']) 
def portfolio():
    # site portfolio
    form = ContactForm()
    if form.validate_on_submit():
        bring = ContactUs(name=bleach.clean(form.name.data), email=bleach.clean(form.email.data), subject=bleach.clean(form.subject.data), message=bleach.clean(form.message.data))
        db.session.add(bring)
        db.session.commit()
        flash('Your message has been sent!', 'success')
        return redirect(url_for('main.portfolio'))
    return render_template('portfolio.html', form=form)

@main.route("/") 
@main.route("/home")
def home():
    #site home
    posts = Post.query.order_by(Post.date_posted.desc())
    return render_template('index.html', posts=posts, title='Home')

@main.route("/about")
def about():
    #about
    posts = Post.query.all()
    return render_template('about.html', title='About', posts=posts, directive='noindex')

@main.route("/submit")
def submit():
    #submit posts
    return render_template('submit.html', title='Submit Post')

@main.route("/contact", methods=['GET', 'POST'])
def contact():
    #contact form
    posts = Post.query.all()
    form = ContactForm()
    if form.validate_on_submit():
        bring = ContactUs(name=bleach.clean(form.name.data), email=bleach.clean(form.email.data), subject=bleach.clean(form.subject.data), message=bleach.clean(form.message.data))
        db.session.add(bring)
        db.session.commit()
        flash('Your message has been sent!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html', title='Contact', form=form, posts=posts, directive='noindex')

@main.route("/admin")
def admin():
    #admin route
    return render_template('admin/index.html')


@main.route("/privacy")
def privacy():
    #privacy policy
    posts = Post.query.all()
    return render_template('privacy.html', title='Privacy Policy', posts=posts, directive='noindex')


@main.route("/terms")
def terms():
    #Terms and Conditions
    posts = Post.query.all()
    return render_template('terms.html', title='Terms and Conditions', posts=posts, directive='noindex')

@main.route("/sitemap.xml")
def sitemap():
    #sitemap route
    return render_template('sitemap.xml')


@main.route("/robots.txt")
def robots():
    #robots directive
    return render_template('robots.txt')



@main.route("/resources")
def resources():
    #resource page
    posts = Post.query.all()
    return render_template('resource_page.html', title='Resource Page', posts=posts)