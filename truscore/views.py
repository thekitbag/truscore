from flask import session, render_template, request, redirect, url_for, json
from truscore import app, db
from .models import User
from .forms import SignupForm, LoginForm

@app.route("/")
def index():
  if 'email' not in session:
    return render_template("index.html") 
  else: 
    return redirect(url_for('loggedInHomePage', name=session.get('name')))

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'email' in session:
    return redirect(url_for('loggedInHomePage', name=session.get('name')))

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
      return redirect(url_for('loggedInHomePage', name=session.get('name')))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('loggedInHomePage', name=session.get('name')))

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
        return redirect(url_for('loggedInHomePage', name=session.get('name')))
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
def loggedInHomePage():
  if 'email' in session:
    return render_template('search.html', name=session.get('name'))
  else:
    return redirect(url_for('index'))



