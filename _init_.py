from flask import Flask, render_template, request
from workflow import *


app = Flask(__name__)

app.config.from_object('config')

model_pickle = "rnn/rnn.pickle"
vectors_pickle = "rnn/vectors_100d.pickle"

RNN = load_model(model_pickle, vectors_pickle)


import views