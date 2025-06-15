from flask import render_template
from flask_login import login_required
from . import wvar_main

@wvar_main.route('/')
@wvar_main.route('/index')
def wr_index():
    return render_template('index.html', title='Home')

@wvar_main.route('/dashboard')
@login_required
def wr_dashboard():
    return render_template('dashboard.html', title='Dashboard') 