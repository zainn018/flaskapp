from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///firstapp.db"
with app.app_context():
   db=SQLAlchemy(app)
class FirstApp(db.Model):
   sno=db.Column(db.integer,primary_key=True,autoincrement=True)
   fname=db.Column(db.String(100),nullable=False)
   lname=db.Column(db.String(100),nullable=False)
   email=db.Column(db.String(100),nullable=False)
   def __repr__(self):
      return f"{self.sno} - {self.fname}"
   
   

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/home')
def homepage():
    return 'Welcome to Homepage'

if __name__=="__main__":
 app.run(debug=True,port=5000)