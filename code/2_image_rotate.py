# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:20:02 2019

@author: lenovo
"""

from scipy import ndimage, misc
import numpy as np
import os
import cv2
import imageio

def main():
    outPath = r"C:\Users\lenovo\Desktop\major\TRAINING_SET\50"
    path = r"C:\Users\lenovo\Desktop\major\data"

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        image_to_rotate = imageio.imread(input_path)

        # rotate the image
        rotated = ndimage.rotate(image_to_rotate, 270)

        # create full output path, 'example.jpg' 
        # becomes 'rotate_example.jpg', save the file to disk
        fullpath = os.path.join(outPath, 'rotated_'+image_path)
        #fullpath = os.path.join(outPath, 'rotated_image')
        imageio.imsave(fullpath, rotated)

if __name__ == '__main__':
    main()