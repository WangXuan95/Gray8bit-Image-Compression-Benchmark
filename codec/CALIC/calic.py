# -*- coding: utf-8 -*-
# Python3


import os
import sys
import time
import numpy as np
from PIL import Image



def loadImage (image_file_name) :
    img = Image.open(image_file_name)
    img_mono = img.convert('L')
    img.close()
    return np.asarray(img_mono)



NUMBER = int(time.time() * 10000000)

CALIC8E_NAME = 'calic8e.exe'
CALIC8D_NAME = 'calic8d.exe'
TMP_RAW_NAME = 'tmp%d.raw' % NUMBER



USAGE_STRING = '''
Encode :
    python %s  -e  <in_file_name>  <out_file_name(.calic)>  <near>
Decode :
    python %s  -d  <in_file_name(.calic)>  <out_file_name(.raw)>
Note :
    ensure that %s, %s and %s are in the same directory
''' % (sys.argv[0], sys.argv[0], CALIC8E_NAME, CALIC8D_NAME, sys.argv[0])



if __name__ == '__main__' :
    
    # check that OS is Windows ------------------------------------------------------------------------
    if not sys.platform.lower().startswith('win') :
        print(USAGE_STRING)
        print('*** error : only support Windows!')
        exit(-1)
    
    
    # parse command line args  ------------------------------------------------------------------------
    try :
        direction = sys.argv[1].lower()
        assert direction in ['e', '-e', 'd', '-d']
        direction = direction[-1]
        src_path = sys.argv[2]
        dst_path = sys.argv[3]
        if direction == 'e' :
            near = int(sys.argv[4])
    except :
        print(USAGE_STRING)
        exit(-1)
    
    
    # parse work directory ------------------------------------------------------------------------
    work_directory, _ = os.path.split(sys.argv[0])
    
    work_directory = work_directory.replace('/', os.path.sep)
    
    if work_directory == '' :
        work_directory = '.'
    
    if not work_directory.endswith(os.path.sep) :
        work_directory += os.path.sep
    
    
    # get full paths ------------------------------------------------------------------------
    raw_path = work_directory + TMP_RAW_NAME
    
    if direction == 'e' :
        exe_path = work_directory + CALIC8E_NAME
    else :
        exe_path = work_directory + CALIC8D_NAME
    
    
    # check existance of exe file ------------------------------------------------------------------------
    if not os.path.isfile(exe_path) :
        print('*** error : %s not exist!' % exe_path)
        exit(-1)
    
    
    if direction == 'e' :
        
        # convert image to 8-bit raw file ------------------------------------------------------------------------
        try :
            img = loadImage(src_path)
        except :
            print('*** error : cannot open %s as a image file!' % src_path)
            exit(-1)
        
        if img.dtype != np.uint8 :
            print('*** error : %s is not 8-bit image!' % src_path)
            exit(-1)
        
        h, w = img.shape
        
        img_bytes = img.tobytes()
        
        with open(raw_path, 'wb') as fp :
            fp.write(img_bytes)
        
        # call exe to do CALIC compression ------------------------------------------------------------------------
        command = '%s %s %d %d 8 %d %s' % (exe_path, raw_path, w, h, near, dst_path)
        print('run command> %s' % command)
        os.system(command)
        
        # remove temp file
        os.remove(raw_path)
        
    else :
        # call exe to do CALIC compression ------------------------------------------------------------------------
        command = '%s %s %s' % (exe_path, src_path, dst_path)
        print('run command> %s' % command)
        os.system(command)




























