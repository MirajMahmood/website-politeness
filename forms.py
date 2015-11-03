from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired



class classifyForm(Form):
	sentence = TextAreaField("Sentence :", validators=[DataRequired()])
	score = StringField("Score :")
	submit = SubmitField("Classify")
	give_feedback = SubmitField("Correct us?")

class feedbackForm(Form):

	polite_button = SubmitField("Polite")
	neutral_button = SubmitField("Neutral")
	impolite_button = SubmitField("Impolite")