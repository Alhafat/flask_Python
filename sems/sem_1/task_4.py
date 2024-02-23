"""
Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/<line>/')
def length(line: str):
    return f"{len(line)}"


if __name__ == '__main__':
    app.run(debug=True)
