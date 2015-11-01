
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
				if class_[0]>class_[1]:
					form.score.data = "impolite"
				else:
					form.score.data = "polite"
			else:
				form.score.data = "error"
			return render_template("home.html", form=form, feedback_form=feedback_form)
	return render_template("home.html", form=form, feedback_form=None)

@app.route('/test/') #/test/ will lead urls /test & /test/
def test():
	return render_template("test.html")
