# -*- coding: utf-8 -*-
"""
Implement an unsharp masking operation (http://en.wikipedia.org/wiki/Unsharp_masking) by 
blurring an image and then subtracting the blurred version from the original. This
gives a sharpening effect to the image. Try this on both color and grayscale images.
"""

from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *


im_gray = array(Image.open(os.path.abspath("data\goldengate.jpg")).convert('L'))
im_rgb = array(Image.open(os.path.abspath("data\goldengate.jpg")))


# grayscale image
gray_blurred = filters.gaussian_filter(im_gray,2)
#imshow(gray_blurred,cmap='gray')

gray_detail = 0.5*im_gray - 0.5*gray_blurred
imshow(gray_detail,cmap='gray') 
sharpened_gray = im_gray + gray_detail
imshow(sharpened_gray,cmap='gray')

# color image
sharpened_rgb = zeros(im_rgb.shape)
for i in range(3):
    blurred_channel = filters.gaussian_filter(im_rgb[:,:,i],1)
    channel_detail = 0.5*im_rgb[:,:,i] - 0.5*blurred_channel
    sharpened_rgb[:,:,i] = im_rgb[:,:,i] + channel_detail
sharpened_rgb = uint8(sharpened_rgb)   
imshow(sharpened_rgb)





