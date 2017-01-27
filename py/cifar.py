#! /usr/bin/env python

NUM_LABELS = 10


def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

def read_batch():
  dict = unpickle('assets/cifar-10-batches-py/data_batch_1')
  data = dict['data']
  labels = dict['labels']
  return (data,labels)

def build_subset(samples_per_set = 4):

  data,labels = read_batch()
  samples = {}

  samples_remaining = samples_per_set * NUM_LABELS

  image_index = 0
  while samples_remaining > 0:

    image = data[image_index]
    label = labels[image_index]
    image_index += 1

    if not samples.has_key(label):
      samples[label] = []

    sample = samples[label]
    if len(sample) == samples_per_set:
      continue

    print "label:",label,"image:",image,"length:",image.size

    sample.append(image)
    samples_remaining -= 1


build_subset()
