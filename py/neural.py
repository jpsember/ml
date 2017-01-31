#! /usr/bin/env python

# Represent a neural network using numpy;
# train it to assign colors to the 'spiral' points
#

from common import *

# Size of hidden layer
H = 100
SEED = 76
D = 3   # note: we are including bias component 1.0
K = NUM_CLASSES

class App:

  def run(self):
    np.random.seed(SEED)
    self.generate_samples()
    self.perform_training()
    self.evaluate_training_set_accuracy()


  def perform_training(self):
    X,y = self.train_samples,self.train_types

    self.W = 0.01 * np.random.randn(D,H)
    self.W2 = 0.01 * np.random.randn(H,K)

    # some hyperparameters
    step_size = 1e-0

    # regularization strength
    reg = 1e-3

    # gradient descent loop
    num_examples = X.shape[0]
    for i in xrange(4000):

      # evaluate class scores, [N x K]
      hidden_layer = np.maximum(0, np.dot(X, self.W)) # note, ReLU activation
      scores = np.dot(hidden_layer, self.W2)

      # compute the class probabilities
      exp_scores = np.exp(scores)
      probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True) # [N x K]

      # compute the loss: average cross-entropy loss and regularization
      corect_logprobs = -np.log(probs[range(num_examples),y])
      data_loss = np.sum(corect_logprobs)/num_examples
      reg_loss = 0.5*reg*np.sum(self.W*self.W) + 0.5*reg*np.sum(self.W2*self.W2)
      loss = data_loss + reg_loss
      if i % 1000 == 0:
        print "iteration %d: loss %s" % (i, df(loss))

      # compute the gradient on scores
      dscores = probs
      dscores[range(num_examples),y] -= 1
      dscores /= num_examples

      # backpropate the gradient to the parameters
      # first backprop into parameters W2 and b2
      dW2 = np.dot(hidden_layer.T, dscores)
      # next backprop into hidden layer
      dhidden = np.dot(dscores, self.W2.T)
      # backprop the ReLU non-linearity
      dhidden[hidden_layer <= 0] = 0
      # finally into W
      dW = np.dot(X.T, dhidden)

      # add regularization gradient contribution
      dW2 += reg * self.W2
      dW += reg * self.W

      # perform a parameter update
      self.W += -step_size * dW
      self.W2 += -step_size * dW2


  def generate_samples(self):
    X,y = build_spiral_data(50,NUM_CLASSES)
    X = np.c_[X,np.ones(X.shape[0])]
    self.train_samples,self.train_types = X,y


  def evaluate_training_set_accuracy(self):
    X,y = self.train_samples, self.train_types
    hidden_layer = np.maximum(0, np.dot(X, self.W))
    scores = np.dot(hidden_layer, self.W2)
    predicted_class = np.argmax(scores, axis=1)
    print 'training accuracy: %s' % df(np.mean(predicted_class == y))



App().run()
