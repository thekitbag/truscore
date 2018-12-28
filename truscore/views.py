from flask import session, render_template, request, redirect, url_for, json
from truscore import app, db
from .models import User, Vote
from .forms import SignupForm, LoginForm, SearchForm
from .search import Truscore, AggregateResults
import datetime

@app.route("/")
def index():
  form = SearchForm()
  if 'email' not in session:
    return render_template("index.html", form=form) 
  else: 
    return redirect(url_for('search', form=form, name=session.get('name')))

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'email' in session:
    return redirect(url_for('search', name=session.get('name')))

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      session['email'] = newuser.email
      session['name'] = newuser.firstname
      return redirect(url_for('search', name=session.get('name')))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('search', name=session.get('name')))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data 
      password = form.password.data 

      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data
        session['name'] = user.firstname
        return redirect(url_for('search', name=session.get('name')))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  session.pop('name', None)
  return redirect(url_for('index'))

@app.route("/search", methods=["GET", "POST"])
def search():
    if 'email' in session:
      query = 'dummy data'
      results = AggregateResults.collateResults(query)
      return render_template('search.html', name=session.get('name'), searchResults=results)
    else:
      return redirect(url_for('index'))

@app.route("/getMoreInfo", methods=["GET", "POST"])
def getMoreInfo():
  more_info = Test.getMoreInfo()
  return json.dumps(more_info)


@app.route("/sendRating", methods=["GET", "POST"])
def sendRating():
  rating = int(request.json['score'])
  establishment = str(request.json['establishment'])
  email = str(session['email'])
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d")
  vote = Vote(today, rating, email, establishment)
  db.session.add(vote)
  db.session.commit()
  return "success"





