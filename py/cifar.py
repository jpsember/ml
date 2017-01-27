#! /usr/bin/env python

from tools import *
import cPickle
from PIL import Image

NUM_LABELS = 10

def unpickle(file):
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
  """Build a subset of the cifar dataset.  Returns a list of lists of sample images"""

  data,labels = read_batch()
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


samples = build_subset()
src_pix = samples[0][1]
dest_pix = crop_cifar(src_pix,32,32,8,8)
image = generate_image(dest_pix,8,8)
image.save('cropped.png')

