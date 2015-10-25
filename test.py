from py4j.java_gateway import JavaGateway
import py4j.java_gateway as gateway
from Model import Model
from request import Request
import numpy as np
import pickle

def classify(text):
    # Make a gateway
    connection = JavaGateway()
    # Send a string and get back the Treepack object
    treepack = connection.entry_point.parse(text)

    # Classify the treepack
    print gateway.get_field(treepack, 'count')
    print gateway.get_field(treepack, 'first')
    print gateway.get_field(treepack, 'second')

if __name__ == '__main__':
    #####################################
    # don't change this
    np.random.seed(43)
    # hyper parameters to be tweaked here
    training_size = 2109  # maximum of 2110 cleaned and all
    l_rate = 0.001
    mini_batch_size = 1
    reg_cost = 0.001
    epochs = 200
    dim = 100
    ######################################

    # perform 60-15-25 percent split into train-val-test sets
    train = np.ceil(0.6 * training_size)
    val = np.ceil(0.15 * training_size)
    test = training_size - train - val

    # load parsed trees from file in PTB format
    with open('rnn.pickle', 'rb') as pickle_file:
        RNN = pickle.load(pickle_file)

    treepack = classify("The request comes here. Pass it to the TreeMaker.")

    if gateway.get_field(treepack, 'count') == 1:
        # Some way to deal with this
    elif gateway.get_field(treepack, 'count') == 2:
        # Some way to deal with this
