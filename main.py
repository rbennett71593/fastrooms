from flask import *
from jinja2 import Template
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

appname = "FastRooms"
build = "0.1"


#----DATABASE TABLES----
class Reservation(db.Model):
    __tablename__ = 'res'
    rID = db.Column(db.Integer, primary_key=True)
    cID = db.Column(db.Integer)
    inDate = db.Column(db.Date)
    outDate = db.Column(db.Date)
    roomNumber = db.Column(db.String)
    #tags = db.relationship('Tag', secondary=enrollment,
    #                            backref=db.backref('courses',lazy='dynamic'))

class Rooms(db.Model):
    __tablename__ = 'rooms'
    roomNumber = db.Column(db.String, primary_key=True)
    occupancy = db.Column(db.Integer)
    occupied = db.Column(db.Boolean)
    dirty = db.Column(db.Boolean)

class Guests(db.Model):
	__tablename__ = 'guests'
	gID = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	address = db.Column(db.String)
	phone = db.Column(db.String)
#--------



#----PAGES----
@app.route('/res')
def res_page():
	title = "Reservations"
	return render_template('display.html',appname=appname,title=title)

@app.route('/op')
def operations_page():
	title = "Operations"
	return render_template('display.html',appname=appname,title=title)

@app.route('/hk')
def housekeeping_page():
	title = "Housekeeping Overview"
	return render_template('display.html',appname=appname,title=title)
	

#Pretty 404 page
@app.errorhandler(404)
def error404(e):
	return render_template('404.html',appname=appname,build=build), 404
	
if __name__ == '__main__':
	app.run()