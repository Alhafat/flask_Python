"""
Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму
"""
from flask import Flask

app = Flask(__name__)

@app.route('/summ/')
def summ(num_1: int = 2, num_2: int = 3) -> str:
    return f"{num_1} + {num_2} = {num_1 + num_2}"

if __name__ == '__main__':
    app.run(debug=True)


