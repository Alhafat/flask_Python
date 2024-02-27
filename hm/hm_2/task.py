"""
Задание

Создать страницу, на которой будет форма для ввода имени и электронной почты,
при отправке которой будет создан cookie-файл с данными пользователя,
а также будет произведено перенаправление на страницу приветствия,
где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл
с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

app.secret_key=b'04383562a427b038eb3cbfd160c821b33a25b7bdb4b5d78d98e3f838bd8c990b'

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return redirect(url_for('index'))
    logout()
    return render_template('form.html')


@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        if not request.form['email']:
            flash('Введите email!', 'danger')
            return redirect(url_for('form'))
        name = request.form['name']
        email = request.form['email']
        session[f'{name}'] = name, email
        return render_template('greeting.html', name=name, email=email)
    return render_template('form.html')

def logout():
    session.pop('username', None)


if __name__ == '__main__':
    app.run(debug=True)