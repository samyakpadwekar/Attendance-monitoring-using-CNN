# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:49:18 2019

@author: lenovo
"""

from PIL import Image
import os, sys

path = r"C:\Users\lenovo\Desktop\major\data\rotated"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((150,150), Image.ANTIALIAS)
            imResize.save(f + ' resized123.jpg', 'JPEG', quality=90)

resize()