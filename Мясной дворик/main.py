from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysnoidvorik.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(db.LargeBinary, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
@app.route('/')
def index():
    return render_template('основные/index.html')

@app.route('/полуфабрикаты')
def pf():
    return render_template('основные/полуфабрикаты.html')

@app.route('/приправы')
def prip():
    return render_template('основные/приправы.html')

@app.route('/соусы')
def sous():
    return render_template('основные/соусы.html')

@app.route('/admin')
def admin():
    return render_template('основные/admin.html')

if __name__ == "__main__":
    app.run(debug=True)