# sript for zomming in images
# first argument is file name
# secound argument is zoom amount 
# third argument (optional) name of output file

import PIL.Image as im
import sys
import math
import scipy.ndimage as nd
import numpy as np

img = im.open("/data/%s" % sys.argv[1])

h, w = img.size[:2]

s = float(sys.argv[2])

zoomed = nd.affine_transform(img, [1-s,1-s,1], [h*s/2,w*s/2,0], order=1)

outfile = sys.argv[1]

if len(sys.argv) > 3:
  outfile = sys.argv[3]

im.fromarray(np.uint8(zoomed)).save("/data/%s" % outfile)

