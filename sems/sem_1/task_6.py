"""
Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def students():
    data = {
        "first_name": ["ivan", "petr", "alex"],
        "last_name": ["ivanov", "petrov", "sidenav"],
        "age": [18, 19,20]
        }

    return render_template('/students.html/', data=data)

if __name__ == '__main__':
    app.run(debug=True)
