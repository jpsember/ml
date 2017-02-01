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

    self.experiment(); return

    self.generate_samples()
    self.perform_training()
    self.evaluate_training_set_accuracy()


  def perform_training(self):
    X,y = self.train_samples,self.train_types

    self.W  = 0.01 * np.random.randn(D,H)
    self.W3 = 0.01 * np.random.randn(H,K)

    reg_strength = 1e-3

    num_examples = X.shape[0]
    for i in xrange(4000):

      # evaluate class scores, [N x K]
      W2 = np.maximum(0, np.dot(X, self.W)) # note, ReLU activation
      scores = np.dot(W2, self.W3)

      # compute the class probabilities
      exp_scores = np.exp(scores)
      probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True) # [N x K]

      # compute the loss: average cross-entropy loss and regularization
      training_logprops = -np.log(probs[range(num_examples),y])

      data_loss = np.sum(training_logprops) / num_examples
      reg_loss = 0.5 * reg_strength * np.sum(self.W * self.W) + 0.5 * reg_strength * np.sum(self.W3 * self.W3)
      loss = data_loss + reg_loss

      if i % 1000 == 0:
        print "iteration %d: loss %s" % (i, df(loss))

      # compute the gradient on scores
      dscores = probs
      dscores[range(num_examples),y] -= 1
      dscores /= num_examples

      # backpropate the gradient to the parameters

      # first backprop into parameters W3
      dW3 = np.dot(W2.T, dscores)

      # next backprop into hidden layer
      dW2 = np.dot(dscores, self.W3.T)

      # backprop the ReLU non-linearity
      dW2[W2 <= 0] = 0

      # finally into W
      dW = np.dot(X.T, dW2)

      # add regularization gradient contribution
      dW3 += reg_strength * self.W3
      dW += reg_strength * self.W

      # perform a parameter update
      step_size = 1.0
      self.W += -step_size * dW
      self.W3 += -step_size * dW3


  def generate_samples(self):
    X,y = build_spiral_data(50,NUM_CLASSES)
    X = np.c_[X,np.ones(X.shape[0])]
    self.train_samples,self.train_types = X,y


  def evaluate_training_set_accuracy(self):
    X,y = self.train_samples, self.train_types
    W2 = np.maximum(0, np.dot(X, self.W))
    scores = np.dot(W2, self.W3)
    predicted_class = np.argmax(scores, axis=1)
    print 'training accuracy: %s' % df(np.mean(predicted_class == y))


  def rand_mat(self, rows, cols=1, mag=8):
    """Generate matrix of random floats, snapped to integer values"""
    m = (np.random.rand(rows,cols) * mag)
    return np.floor(m)



  def experiment(self):

    num_samples = 6
    k = 4

    m = self.rand_mat(num_samples,k)
    print "Samples:\n",m

    types = self.rand_mat(num_samples,1,k).astype(int)
    print "Types:\n",types


    # Generate Multiclass Support Vector Machine (SVM) loss

    # Pre-allocate matrix... unnecessary optimization?
    #
    svm_loss = np.empty([num_samples,1])

    for row_num in range(num_samples):
      src_row = m[row_num]

      # Use a list comprehension... is there a better way?

      res = [max(0,
         score_for_type             # score from function
         - src_row[types[row_num]]  # true score for sample
          + 1
        ) for score_for_type in src_row]

      # Subtract additional 1.0 since we've included loss for the sample's true type,
      # which we actually want to exclude

      svm_loss[row_num] = sum(res) - 1.0

    print "SVM loss:\n",svm_loss




App().run()
