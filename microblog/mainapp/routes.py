#!/usr/bin/env python3
'''Routes module
   contains all routes for the website
'''
from flask import render_template, flash, redirect, url_for
from mainapp import app
from mainapp.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    '''Index view function
       return
           home page of the website
    '''
    user = {'username': 'Sphesihle'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])

def login():
    '''
       login view function
    '''
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
