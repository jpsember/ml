# Attempt to access the CIFAR dataset, and convert a few images to jpg...

def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

dict = unpickle('assets/cifar-10-batches-py/data_batch_1')
print 'dict size:',dict
