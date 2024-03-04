from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), unique=True, nullable=False)
    lastName = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, firstName, lastName, password, email):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email

    def __repr__(self, id, firstName, lastName, password, email):
        return (f'User('
                f'{self.id}, '
                f'{self.firstName}, '
                f'{self.lastName}, '
                f'{self.password}, '
                f'{self.email}, '
                f')')