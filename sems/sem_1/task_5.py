"""
Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
