from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from . import wvar_auth
from ..models import wvar_User
from .. import wvar_db

@wvar_auth.route('/login', methods=['GET', 'POST'])
def wr_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = wvar_User.query.filter_by(username=username).first()
        
        if user is None or not user.wfun_check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('wvar_auth.wr_login'))
            
        login_user(user)
        return redirect(url_for('wvar_main.wr_dashboard'))
        
    return render_template('auth/login.html', title='Sign In')

@wvar_auth.route('/logout')
@login_required
def wr_logout():
    logout_user()
    return redirect(url_for('wvar_main.wr_index')) 