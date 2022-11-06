from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

from app import api
from app.api.api_user import GetUser, AddUser, UpdateUser, DeleteUser


@app.route('/')
@app.route('/index')
def hello_world():  # put application's code here
    return render_template('index.html', text='Hello World!')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


# api route for CRUD user
api.add_resource(GetUser, '/get')
api.add_resource(AddUser, '/add')
api.add_resource(UpdateUser, '/update/<int:id>')
api.add_resource(DeleteUser, '/delete/<int:id>')

if __name__ == '__main__':
    app.run()
