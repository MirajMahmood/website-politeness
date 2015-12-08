from __future__ import division
from _init_ import *
from forms import *


def classify_politeness(vector):
	if abs(vector[0]-vector[1]) <0.21:
		return "Neutral"
	elif vector[0]>vector[1]:
		return "Impolite"
	else:
		return "Polite"

@app.route('/', methods=['GET', 'POST'])
def home_page():
	form = classifyForm()
	feedback_form = feedbackForm()

	if request.method =='POST':
		class_ = classify(str(form.sentence.data.lower()), RNN)

		if class_ is not None:
			form.score.data = classify_politeness(class_)
			
		else:
			class_ = [0,0]
			for i in form.sentence.data.split('.'):
				if i != "":
					res = classify(i, RNN)
					class_[0] += res[0]
					class_[1] += res[1]

			sen_len = form.sentence.data.split('.')
			try:
				class_[0] /= sen_len
				class_[1] /= sen_len
			except:
				#if the sentence length is 0 then class_ should be [0,0] which it already is 
				pass

			form.score.data = classify_politeness(class_)
		
		return render_template("home.html", form=form, feedback_form=feedback_form)

	return render_template("home.html", form=form, feedback_form=None, color='#40b3ff')


@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():

	text = request.form['sentence']
	label = 0
	if "polite_button" in request.form:
		label = 1
	elif "impolite_button" in request.form:
		label = 0
	elif "neutral_button" in request.form:
		label = 0.5
		
	else:
		return "nothing"

	record_feedback(text, label, writer)
	return "Thank you for your feedback"


@app.route('/about/')
def about():
	return render_template("about.html")
