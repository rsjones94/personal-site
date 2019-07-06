
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField
 
class ContactForm(FlaskForm):
  name = StringField("Name", validators=[DataRequired()])
  email = EmailField("Email", validators=[DataRequired(), Email()])
  subject = StringField("Subject", validators=[DataRequired()])
  message = TextAreaField("Message", validators=[DataRequired()])
  submit = SubmitField("Send")