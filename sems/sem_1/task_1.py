"""
Напишите простое веб-приложение на Flask, которое будет
выводить на экран текст "Hello, World!".
"""

from flask import Flask

app = Flask(__name__)


@app.route('/index/')
def index():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    index()
    app.run(debug=True)
