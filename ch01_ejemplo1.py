# -*- coding: utf-8 -*-
"""
Graficar puntos y lineas sobre una imagen
"""

from PIL import Image
from pylab import *
import os

# read image to array
im = array(Image.open(os.path.abspath("data\space.jpg")))

# plot the image
imshow(im)

# some points
x = [100,120,500,550,300]
y = [50,300,50,200,250]

# plot the points with green circle-markers
plot(x,y,'yo')

# line plot connecting the second and third points
plot(x[1:3],y[1:3],'g--')

# add title and show the plot
title('Plotting: "space.jpg"')
show()




