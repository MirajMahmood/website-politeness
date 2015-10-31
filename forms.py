from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired



class classifyForm(Form):
	sentence = TextAreaField("Sentence :", validators=[DataRequired()])
	score = StringField("Score :")
	submit = SubmitField("Classify")
	give_feedback = SubmitField("Correct us?")

class feedbackForm(Form):

	feedback_classification = StringField("Classification :")
	submit = SubmitField("Okay!")