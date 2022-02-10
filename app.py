from flask import Flask, render_template, request, redirect
from models import db, StudentModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/agregar', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('form.html')

    if request.method == 'POST':
        student_id = request.form['code']
        name = request.form['name']
        age = request.form['age']
        student = StudentModel(code=student_id, name=name, age=age)
        db.session.add(student)
        db.session.commit()
        return redirect('/')

@app.route('/')
def index():
    students = StudentModel.query.all()
    return render_template('index.html', students=students)

if __name__ == "__main__":
    app.run(host='localhost')