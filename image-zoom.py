# sript for zomming in images
# first argument is file name
# secound argument is zoom amount 
# third argument (optional) name of output file

import PIL.Image as im
import sys
import math

img = im.open("/data/%s" % sys.argv[1])

zoom = 1 + float(sys.argv[2])

originSize = img.size[0], img.size[1]

largeSize = int(math.ceil(img.size[0] * zoom)), int(math.ceil(img.size[1] * zoom))

imgLarge = img.resize(largeSize)

hDiff = int(math.floor((largeSize[0] - originSize[0]) / 2))
vDiff = int(math.floor((largeSize[1] - originSize[1]) / 2))

zoomBox = ( \
  hDiff, \
  vDiff, \
  originSize[0] + hDiff, \
  originSize[1] + vDiff  \
)

imgZoomed = imgLarge.crop(zoomBox)

outfile = sys.argv[1]

if len(sys.argv) > 3:
  outfile = sys.argv[3]

imgZoomed.save("/data/%s" % outfile)

