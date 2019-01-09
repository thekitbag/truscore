from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from truscore import db, app, es



class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)


class Vote(db.Model):
  #this will be deprecated soon
  __tablename__ = 'votes'
  uid = db.Column(db.Integer, primary_key = True)
  date = db.Column(db.String(100))
  vote = db.Column(db.String(100))
  username = db.Column(db.String(120), unique=True)
  product_name = db.Column(db.String(100))
  product_top_1 = db.Column(db.String(100))
  product_top_2 = db.Column(db.String(100))
  product_top_3 = db.Column(db.String(100))
  product_bottom_1 = db.Column(db.String(100))
  product_bottom_2 = db.Column(db.String(100))
  product_bottom_3 = db.Column(db.String(100))
  comments = db.Column(db.String(160))

  def __init__(self, date, vote, username, product_name, product_top_1, product_top_2, product_top_3, product_bottom_1, product_bottom_2, product_bottom_3, comments):
    self.date = date
    self.vote = vote
    self.username = username
    self.product_name = product_name
    self.product_top_1 = product_top_1
    self.product_top_2 = product_top_2
    self.product_top_3 = product_top_3
    self.product_bottom_1 = product_bottom_1
    self.product_bottom_2 = product_bottom_2
    self.product_bottom_3 = product_bottom_3
    self.comments = comments
    es.index(index='products', doc_type='establishment', body={'text': product_name})

class Rating(db.Model):
  __tablename__ = 'votes'
  

  def __init__(self, date, vote, username, establishment):
    self.date = date
    self.vote = vote
    self.username = username
    self.establishment = establishment
    es.index(index='establishments', doc_type='establishment', body={'text': establishment})



