from . import auth
from flask import Flask, request, render_template, redirect, flash, url_for
from ..models import User, Admin
from app import db


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        phone_number = int(request.form['phone_number'])

        user = User.query.filter_by(username=username).first()
        if user:
            flash('This username already exists . please choose another username')
            return redirect(url_for('auth.signup'))
        new_user = User(fullname=fullname, username=username, email=email, phone_number=phone_number)
        db.session.add(new_user)
        db.session.commit()
        flash('Account registered successfully', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
