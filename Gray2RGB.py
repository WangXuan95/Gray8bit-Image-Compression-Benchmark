# -*- coding:utf-8 -*-
# Python3
# This script is to convert gray 8-bit images (.pgm) to RGB888 images (.ppm).
# The method is: fill the original gray 8-bit channel to the RGB888's green channel, and set the red and blue channel to all zero.

import sys
import os
import numpy as np
from PIL import Image


def createDirectoryIfNotExist (directory) :   # function: check if directory exist. If so, print error and exit. If not, create one.
    os.system('cd .')
    if os.path.exists(directory) :
        print('***Error: %s already exists' % directory)
        exit(1)
    else :
        os.mkdir(directory)


def convertPGM2PPM (src_path, dst_path) :
    try :
        img_gray = Image.open(src_path)
        arr_gray = np.asarray(img_gray)
        img_gray.close()
        h, w = arr_gray.shape
        arr_rgb = np.zeros([h,w,3], dtype=arr_gray.dtype)
        arr_rgb[:,:,1] = arr_gray
        Image.fromarray(arr_rgb).save(dst_path)
        print('processed %s' % src_path)
    except :
        print('skip %s'      % src_path)


if __name__ == '__main__' :
    try :
        dir_in, dir_out = sys.argv[1:3]
    except :
        print('Usage: python %s <input-dir> <output-dir>' % sys.argv[0])
        exit(1)
    
    createDirectoryIfNotExist(dir_out)
    
    for fname in os.listdir(dir_in) :
        fname_prefix, _ = os.path.splitext(fname)
        dst_fname = fname_prefix + '.ppm'
        
        src_path = os.path.join(dir_in, fname)
        dst_path = os.path.join(dir_out, dst_fname)
        
        convertPGM2PPM(src_path, dst_path)
