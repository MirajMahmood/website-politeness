
from _init_ import *
from forms import *



@app.route('/', methods=['GET', 'POST'])
def home_page():
	form = classifyForm()
	feedback_form = feedbackForm()

	if request.method =='POST':
		if form.validate_on_submit():
			class_ = classify(str(form.sentence.data.lower()), RNN)
			if class_ is not None:
				if class_[0]-class_[1] <0.21:
					form.score.data = "Neutral"
				elif class_[0]>class_[1]:
					form.score.data = "Impolite"
				else:
					form.score.data = "Polite"
			
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
@app.route('/test/') #/test/ will lead urls /test & /test/
def test():
	return render_template("test.html")
