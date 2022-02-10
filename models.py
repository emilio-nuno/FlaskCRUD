from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class StudentModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    code = db.Column(db.String(9), unique=True)

    def __init__(self, code, name, age):
        self.code = code
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}:{self.code}"
