# -*- coding: utf-8 -*-

"""
Visualizacion de contornos de una imagen
"""


from PIL import Image
from pylab import *
import os

# read image to array
im = array(Image.open(os.path.abspath("data\space.jpg")).convert('L'))

# create new figure
figure()

# don't use colors
gray()
# show contours with origin upper left corner
contour(im,origin='image')
axis('equal')
axis('off')






