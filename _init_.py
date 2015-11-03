from flask import Flask, render_template, request
from workflow import *


app = Flask(__name__)

app.config.from_object('config')

model_pickle = "rnn/rnn.pickle"
vectors_pickle = "rnn/vectors_100d.pickle"

RNN = load_model(model_pickle, vectors_pickle)

# Keep file open in append mode, this should happen every time the server starts

fh = open('recorded_data.csv', 'a')
writer = csv.writer(fh)

import views