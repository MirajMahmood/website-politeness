import os
import threading
from _init_ import *


def run_java():
	os.system("javac -classpath './WebBackendParser/src:./WebBackendParser/src/stanford-corenlp-full/*:./WebBackendParser/src/py4j0.9.jar:' WebBackendParser/src/TreeMaker.java")
	os.system("java -cp ':./WebBackendParser/src/:./WebBackendParser/src/stanford-corenlp-full/*:./WebBackendParser/src/py4j0.9.jar:' TreeMaker")


thr = threading.Thread(target=run_java)
thr.daemon = True
thr.start()

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
thr.exit()
