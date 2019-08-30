from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TodoForm(FlaskForm):
    listName = StringField('todo', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('add')