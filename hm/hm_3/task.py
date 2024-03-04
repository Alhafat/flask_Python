# from flask import Flask, render_template, request
# from flask_wtf.csrf import CSRFProtect
#
# from hm.hm_3.models import db, User
# from register import RegisterForm
#
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = b'04383562a427b038eb3cbfd160c821b33a25b7bdb4b5d78d98e3f838bd8c990b'
# csrf = CSRFProtect(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'register_user.db'
# db.init_app(app)
#
#
# @app.route('/')
# @app.route('/register/', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     if request.method == 'POST' and form.validate():
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#         password = form.password.data
#         email = form.email.data
#         add_user(first_name, last_name, email, password)
#         print(password)
#
#     return render_template('register.html', form=form)
#
#
# @app.cli.command("init-db")
# def init_db():
#     db.create_all()
#     print("ok")
#
#
# @app.cli.command("/register/")
# def add_user(first_name, last_name, email, password):
#     user = User(first_name=first_name, last_name=last_name, email=email, password=password)
#     db.session.add(user)
#     db.session.commit()
#     print(f"User {first_name} {last_name} added successfully")


from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect

from HW_3.register import RegistrationForm
from HW_3.models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mySecretkeY'
csrf = CSRFProtect(app)
"""
Генерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///registration_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data

        exist_user = User.query.filter(
            (User.firstname == firstname) or (User.lastname == lastname) or (User.email == email)
        ).first()
        if exist_user:
            error_msg = 'Username or email already exists.'
            form.firstname.errors.append(error_msg)
            return render_template('register.html', form=form)
        new_user = User(firstname=firstname, lastname=lastname,
                        email=email)
        new_user.set_pass(password)
        db.session.add(new_user)
        db.session.commit()
        success_msg = 'Registration successful!'
        return success_msg
    return render_template('register.html', form=form)


@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    users = User.query.all()
    return f'{list(users)}'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
