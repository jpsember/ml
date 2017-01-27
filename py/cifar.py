#! /usr/bin/env python

from tools import *
import cPickle
from PIL import Image

NUM_LABELS = 10
SUBSET_PATH = "assets/cifar_subset.bin"

def read_batch(file = SUBSET_PATH):
  fo = open(file, 'rb')
  dict = cPickle.load(fo)
  fo.close()
  data = dict['data']
  labels = dict['labels']
  return (data,labels)

def build_subset(samples_per_set = 4):
  """Build a subset of the cifar dataset.  Returns a list of lists of sample images"""

  data,labels = read_batch('assets/cifar-10-batches-py/data_batch_1')
  samples = []
  for i in range(NUM_LABELS):
    samples.append([])

  samples_remaining = samples_per_set * NUM_LABELS

  image_index = 0
  while samples_remaining > 0:

    image = data[image_index]
    label = labels[image_index]
    image_index += 1

    sample = samples[label]
    if len(sample) == samples_per_set:
      continue

    sample.append(image)
    samples_remaining -= 1

  return samples

def crop_cifar(pixels, src_width, src_height, dest_width, dest_height):
  """Extract a cropped rectangle from a source image (in cifar format)"""
  spix = src_width * src_height
  error_if(len(pixels) != spix * 3, "bad dimensions vs pixel count")
  pout = []
  for plane in range(3):
    index = ((src_height - dest_height) / 2) * src_width + (src_width - dest_width)/2
    index += spix * plane
    i = index
    for y in range(dest_height):
      for x in range(dest_width):
        pout.append(pixels[i + x])
      i += src_width
  return pout

def generate_image(pixels, width, height):
  """Generate an Image from a cifar image"""
  npix = width * height
  error_if(len(pixels) != npix * 3, "bad dimensions vs pixel count")

  pixels_out = []
  index = 0
  for y in range(height):
    for x in range(width):
      tup = (pixels[index],pixels[index+npix],pixels[index+npix*2])
      index += 1
      pixels_out.append(tup)

  image = Image.new("RGB",(width,height))
  image.putdata(pixels_out)
  return image

def generate_cropped_subset(num_labels = 3, generate_png = False):
  """Generate a cropped subset of the cifar images"""
  dict = {}
  data = []
  dict['data'] = data
  labels = []
  dict['labels'] = labels

  samples = build_subset()
  for label_number in range(num_labels):
    for image in samples[label_number]:
      dest_pix = crop_cifar(image,32,32,8,8)
      image = generate_image(dest_pix,8,8)
      if generate_png:
        image.save('subset_' + str(len(data))+'.png')
      data.append(dest_pix)
      labels.append(label_number)

  cPickle.dump(dict, open(SUBSET_PATH, "wb") )


generate_cropped_subset()
data, labels = read_batch(SUBSET_PATH)
print "Generated cropped subset of CIFAR dataset; labels:\n",labels
