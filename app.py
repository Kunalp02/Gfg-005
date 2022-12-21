from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/flask_demo'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Sname = db.Column(db.String(80), unique=True, nullable=False)
    School_Name= db.Column(db.String(120), nullable=False)

    def __init__(self, Sname, School_Name):
        self.Sname = Sname
        self.School_Name = School_Name


@app.route('/')
def home():
    return '<a href="/addStudent"><button> Click here to add student </button></a>'


@app.route("/addStudent")
def addStudent():
    return render_template("index.html")


@app.route("/addStudent", methods=['POST'])
def studentAdd():
    Sname = request.form["sname"]
    School_Name = request.form["school"]
    print(Sname, School_Name)
    entry = Student(Sname, School_Name)
    db.session.add(entry)
    db.session.commit()
    flash('You Have Successfully Added Student')
    return redirect('addStudent')

if __name__ == '__main__':
    db.create_all()
    app.run()
