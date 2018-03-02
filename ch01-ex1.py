# -*- coding: utf-8 -*-

"""
Take an image and apply Gaussian blur like in Figure 1-9. Plot the image contours
for increasing values of σ. What happens? Can you explain why?
"""

from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('data\hotel.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)
im3 = filters.gaussian_filter(im,10)
im4 = filters.gaussian_filter(im,15)


figure()
gray()
contour(im,origin='image')
axis('equal')
axis('off')

figure()
gray()
contour(im2,origin='image')
axis('equal')
axis('off')

figure()
gray()
contour(im3,origin='image')
axis('equal')
axis('off')

figure()
gray()
contour(im4,origin='image')
axis('equal')
axis('off')

