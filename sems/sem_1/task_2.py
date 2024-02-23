"""
Дорабатываем задачу 1.
Добавьте две дополнительные страницы в ваше веб-приложение:
○ страницу "about"
○ страницу "contact".
"""
from flask import Flask

app = Flask(__name__)


@app.route('/about/')
def about():
    return '<h1>ABOUT</h1>'


@app.route('/contact/')
def contact():
    return '<h1>CONTACT</h1>'

if __name__ == '__main__':
    about()
    contact()
    app.run(debug=True)