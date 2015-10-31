import os

def run_java():
	os.system("javac -classpath './WebBackendParser/src:./WebBackendParser/src/stanford-corenlp-full/*:./WebBackendParser/src/py4j0.9.jar:' WebBackendParser/src/TreeMaker.java")
	os.system("java -cp ':./WebBackendParser/src/:./WebBackendParser/src/stanford-corenlp-full/*:./WebBackendParser/src/py4j0.9.jar:' TreeMaker")

run_java()