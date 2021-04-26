from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок новости', validators=[DataRequired()])
    text = TextAreaField("Содержание новости", validators=[DataRequired()])
    submit = SubmitField('Создать новость')
