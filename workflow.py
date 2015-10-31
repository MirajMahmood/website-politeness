import sys, os
import cPickle

from py4j.java_gateway import JavaGateway
import py4j.java_gateway as gateway

import rnn
from rnn.Model import Model
from rnn.request import Request
from rnn.Tree import Tree
from rnn.Node import Node

# Little hack for pickling out objects from a directory:
# ref: http://stackoverflow.com/questions/2121874/python-pickling-after-changing-a-modules-directory
sys.modules['Model'] = rnn.Model
sys.modules['request'] = rnn.request
sys.modules['Tree'] = rnn.Tree
sys.modules['Node'] = rnn.Node

def classify(text, RNN):

    # Make a gateway, end the text and get back a Treepack object
    connection = JavaGateway()
    treepack = connection.entry_point.parse(text)

    # Time to classify!
    treecount = gateway.get_field(treepack, 'count')
    if treecount == 1:
        # Make a tree and classify
        print 'Making tree...'
        tree = Tree(_id=-1)
        tree.root = Node()
        sentence = gateway.get_field(treepack, 'first')
        tree.root.read(sentence, 0, True)
        # Chaipi as usual
        tree.root = tree.root.children[0]

        prediction_vector = RNN.predict_tree(tree)
        print prediction_vector

    elif treecount == 2:
        # Make a request for classification. Note: request = 2 trees
        print 'Making request...'
        request = Request()
        first_sentence = gateway.get_field(treepack, 'first')
        second_sentence = gateway.get_field(treepack, 'second')
        request.add_tree(first_sentence, -1)
        request.add_tree(second_sentence, -1)

        prediction_vector = RNN.predict_request(request)
        print prediction_vector
        
    else:
        # Probably return some kind of error to the client
        prediction_vector = None

    return prediction_vector

def load_model(model_pickle, vectors_pickle):
    # Load hyperparameters
    with open(model_pickle, 'rb') as pickle_file:
        RNN = cPickle.load(pickle_file)

    # Load word vectors
    with open(vectors_pickle, 'rb') as pickle_file:
        Model.word_to_vec = cPickle.load(pickle_file)

    return RNN
'''
if __name__ == '__main__':
    model_pickle = "rnn/rnn.pickle"
    vectors_pickle = "rnn/vectors_100d.pickle"

    RNN = load_model(model_pickle, vectors_pickle)

    treepack = classify("The request comes here. Pass it to the TreeMaker.", RNN)

'''
