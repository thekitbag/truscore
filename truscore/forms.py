from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  submit = SubmitField('Sign up')

class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")

class SearchForm(Form):
  search = StringField('How good is it? Hedgehog it', validators=[DataRequired("Please enter a search term.")])
  submit = SubmitField("Hedgehog it!")

class ReviewNewProductForm(Form):
   product_type = SelectField(
        'What type of product, service or location would you like to review?',
        choices=[
        ({'product type': 'visitable_irl',
          'product category': 'restaurant'
          }, 'Restaurant'),
        ({'product type': 'visitable_irl',
          'product category': 'bar'
          }, 'Bar'),
        ({'product type': 'visitable_irl',
          'product category': 'hotel'
          }, 'Hotel'),
        ({'product type': 'consumable',
          'product category': 'film'
          }, 'Film'),
        ({'product type': 'visitable_online',
          'product category': 'website'
          }, 'Website')
      ]
    )
   product_title = StringField('What is the name of the the product, service or location?', validators=[DataRequired("You must enter the title")])
   rating = SelectField('How would you rate this product, service or location?', choices=[(1,'Awful'), (2, 'Bad'), (3,'OK'), (4,'Good'), (5,'Excellent')])
   top_1 = StringField('What were the three BEST things about this product, service or location? (optional)')
   top_2 = StringField('What were the three BEST things about this product, service or location? (optional)')
   top_3 = StringField('What were the three BEST things about this product, service or location? (optional)')
   bottom_1 = StringField('What were the three best WORST about this product, service or location? (optional)')
   bottom_2 = StringField('What were the three best WORST about this product, service or location? (optional)')
   bottom_3 = StringField('What were the three best WORST about this product, service or location? (optional)')
   comments = TextAreaField('Any other comments? (optional')
   submit = SubmitField("Submit")


