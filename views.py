from _init_ import *
from forms import *

@app.route('/')
def hello():
	return "Hello World"

@app.route('/test/') #/test/ will lead urls /test & /test/
def test():
	return render_template("test.html")