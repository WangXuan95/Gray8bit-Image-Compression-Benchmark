# -*- coding:utf-8 -*-
# Python3
# This script is to pad images' height and width to multiple of 8.

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


def paddingImage (src_path, dst_path, pad=8) :
    try :
        img_gray = Image.open(src_path)
        arr_gray = np.asarray(img_gray)
        img_gray.close()
        h, w = arr_gray.shape
        nh = ((h + (pad-1)) // pad) * pad
        nw = ((w + (pad-1)) // pad) * pad
        arr_gray8 = np.zeros([nh,nw], dtype=arr_gray.dtype)
        arr_gray8[:h,:w] = arr_gray
        Image.fromarray(arr_gray8).save(dst_path)
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
        src_path = os.path.join(dir_in, fname)
        dst_path = os.path.join(dir_out, fname)
        
        paddingImage(src_path, dst_path)
