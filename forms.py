from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField, SelectField, widgets, TextAreaField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import DataRequired, URL, Length, Email, ValidationError


class EnquiryForm(FlaskForm):
    Name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    Message = review_text = TextAreaField("message", validators=[DataRequired(), Length(min=30)])
    submit = SubmitField()

