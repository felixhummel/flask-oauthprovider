# -*- coding: utf-8 -*-
from demoprovider import app
from models import ResourceOwner as User
from models import db_session
from flask import g, session, render_template, request, redirect, flash
from flask import abort, url_for

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.filter_by(id=session['user_id']).first()


@app.after_request
def after_request(response):
    db_session.remove()
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Does one of three things:
    a) render login form
    b) with POST-arguments set: set g.user and redirect to where we came from
    c) with g.user: redirect to where we came from
    """
    next_url = request.args.get('next')
    if g.user is not None:
        return redirect(next_url)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        g.user = User.query.filter_by(name=username, password=password).first()
        if g.user is not None:
            session['user_id'] = g.user.id
            next_url = request.args.get('next')
            return redirect(next_url)
    return render_template('login.html', next=next_url)
