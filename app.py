from config import Config

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./app.db'
db = SQLAlchemy(app)

class FredSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dt = db.Column(db.DateTime)
    booked = db.Column(db.Boolean)

    def __repr__(self):
        return '<Session %r>' % str(self.id)

@app.route("/")
def hello():
	return render_template('hello.html')
