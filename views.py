from _init_ import *
from forms import *

@app.route('/', methods=['GET', 'POST'])
def hello():
	form = classifyForm()
	if request.method =='POST':
		if form.validate_on_submit():
			form.score.data = "score!"
			feedback_form = feedbackForm()
			return render_template("home.html", form=form, feedback_form=feedback_form)
	return render_template("home.html", form=form)

@app.route('/test/') #/test/ will lead urls /test & /test/
def test():
	return render_template("test.html")