from flask import Flask,request,redirect,url_for,flash,render_template



from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append('E:/flask workouts/gym/newfolder')  # Adjust the path accordingly


app = Flask(__name__)

    



    
app.config['SECRET_KEY'] = 'abcde12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

from my1 import routes  
        



        












    


