# -*- coding:utf-8 -*-
# Python3
# This is a script for benchmarking image compression.
# Note: only support Windows system !!

import os
import time

#from PIL import Image   # uncomment this if you are testing JPEG-LS, WEBP, or JPEG2000. If there are any issues, try to use newer version of Pillow (I used Pillow 10.1.0)
#import pillow_jpls      # uncomment this if you are testing JPEG-LS


# Note: specific directories here
#DIR_INPUT   = 'rgb888_example'        # some codec need to input RGB888 image
DIR_INPUT   = 'gray8_example'
DIR_ENCODED = 'encoded'
DIR_DECODED = 'decoded'


# Note: please uncomment one of the lines below to select a codec !!!!!!!!!!!!!!!!!!!!!!!!!
#                        [ encode command                                                                 , decode command                                              ]
ENCODE_CMD, DECODE_CMD = [ r'.\codec\BMF\BMF.exe -s -q9 -O{1} {0}'                                        , r'.\codec\BMF\BMF.exe -pnm -O{1} {0}'                       ]
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\BMF\BMF.exe -s     -O{1} {0}'                                        , r'.\codec\BMF\BMF.exe -pnm -O{1} {0}'                       ]
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\BMF\BMF.exe        -O{1} {0}'                                        , r'.\codec\BMF\BMF.exe -pnm -O{1} {0}'                       ]
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\NBLIC\nblic_codec.exe -ce0t {0} {1}.nblic'                           , r'.\codec\NBLIC\nblic_codec.exe -d  {0} {1}.pgm'            ]
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\NBLIC\nblic_codec.exe -ce1  {0} {1}.nblic'                           , r'.\codec\NBLIC\nblic_codec.exe -d  {0} {1}.pgm'            ]
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\NBLIC\nblic_codec.exe -ce2V {0} {1}.nblic'                           , r'.\codec\NBLIC\nblic_codec.exe -dV {0} {1}.pgm'            ]
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\NBLIC\nblic_codec.exe -ce3V {0} {1}.nblic'                           , r'.\codec\NBLIC\nblic_codec.exe -dV {0} {1}.pgm'            ]
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\JPEG-XL\cjxl.exe {0} {1}.jxl -q 100 -e 7'                            , r'.\codec\JPEG-XL\djxl.exe {0} {1}.pgm'                     ]
#ENCODE_CMD, DECODE_CMD = [r'.\codec\MRP\mrp_enc.exe    {0} {1}.mrp'                                       , r'.\codec\MRP\mrp_dec.exe {0} {1}.pgm'                      ]   # need to pad the image to a multiple of 8 first !!
#ENCODE_CMD, DECODE_CMD = [r'.\codec\MRP\mrp_enc.exe -o {0} {1}.mrp'                                       , r'.\codec\MRP\mrp_dec.exe {0} {1}.pgm'                      ]   # need to pad the image to a multiple of 8 first !!
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\GRALIC\Gralic111d.exe c {1}.gralic {0}'                              , r'.\codec\GRALIC\Gralic111d.exe d {0} {1}.ppm'              ]   # require RGB888 image as input !!
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\LEA\clea.exe {0} {1}.lea'                                            , r'.\codec\LEA\dlea.exe {0} {1}.ppm'                         ]   # require RGB888 image as input !!
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\FLIC\FLIC.exe c {1}.flic {0}'                                        , r'.\codec\FLIC\FLIC.exe d {0} {1}.ppm'                      ]   # require RGB888 image as input !!
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\QLIC2\QLIC2.exe c {1}.qlic2 {0}'                                     , r'.\codec\QLIC2\QLIC2.exe d {0} {1}.ppm'                    ]   # require RGB888 image as input !!
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\HALIC\Halic_Rapid_v_0_6_1_Encode.exe {0} {1}.halic'                  , r'.\codec\HALIC\Halic_Rapid_v_0_6_1_Decode.exe {0} {1}.pgm' ]   # require RGB888 image as input !!
#ENCODE_CMD, DECODE_CMD = [ r'wsl ./codec/FLIF/flif -e -N -E100 {0} {1}.flif'                              , r'wsl ./codec/FLIF/flif -d {0} {1}.pgm'                     ]   # require Windows subsystem of Linux (WSL) !!
#ENCODE_CMD, DECODE_CMD = [ r'wsl ./codec/LOCO_ANS/loco_ans_codec 0 {0} {1}.locoans 0'                     , r'wsl ./codec/LOCO_ANS/loco_ans_codec 1 {0} {1}.pgm'        ]   # require Windows subsystem of Linux (WSL) !!
#ENCODE_CMD, DECODE_CMD = [ r'wsl ./codec/SelectivePMO/pmo_codec -i {0} -b {1}.pmo'                        , r'wsl ./codec/SelectivePMO/pmo_codec -b {0} -o {1}'         ]   # require Windows subsystem of Linux (WSL) !!
#ENCODE_CMD, DECODE_CMD = [ r'.\codec\OPTIPNG\optipng.exe -o2 -force {0} -out {1}.png'                     , r'Image.open(r"{0}").save(r"{1}.pgm")'                      ]   # require Python Pillow !!
#ENCODE_CMD, DECODE_CMD = [ r'Image.open(r"{0}").save(r"{1}.jls", spiff=None)'                             , r'Image.open(r"{0}").save(r"{1}.pgm")'                      ]   # require Python Pillow and pillow_jpls library !!
#ENCODE_CMD, DECODE_CMD = [ r'Image.open(r"{0}").save(r"{1}.webp", lossless=True, quality=100, method=6)'  , r'Image.open(r"{0}").save(r"{1}.pgm")'                      ]   # require Python Pillow library !!
#ENCODE_CMD, DECODE_CMD = [ r'Image.open(r"{0}").save(r"{1}.j2k",format="JPEG2000",irreversible=False)'    , r'Image.open(r"{0}").save(r"{1}.pgm")'                      ]   # require Python Pillow library !!




def printColor (color_code, string) :         # function: print a string with color
    print( ('\033[1;%dm' % color_code) + string + '\033[0m' )


def createDirectoryIfNotExist (directory) :   # function: check if directory exist. If so, print error and exit. If not, create one.
    os.system('cd .')
    if os.path.exists(directory) :
        printColor(31, '***Error: %s already exists' % directory)
        exit(1)
    else :
        os.mkdir(directory)


def runCommand(command) :                     # function: run command/statement in Python, Windows subsystem of Linux (WSL), or Windows CMD
    if   command.startswith('Image.open') :   # is a Python statement
        printColor(32, 'python> '+command)    #
        exec(command)                         #   run as a python statement
    elif command.startswith('wsl') :          # is a Linux command
        command = command.replace('\\', '/')  #   replace Windows '\' to Linux '/'
        printColor(32, '> '+command)          #
        os.system(command)                    #   run command in WSL
    else :                                    # is a Windows command
        printColor(32, '> '+command)          #
        os.system(command)                    #   run command


if __name__ == '__main__' :
    
    createDirectoryIfNotExist(DIR_ENCODED)
    createDirectoryIfNotExist(DIR_DECODED)
    
    if ENCODE_CMD.startswith('wsl') or DECODE_CMD.startswith('wsl') :
        os.system('wsl cd .')                                # touch WSL
    
    printColor(33, '-------------------------- start to encode --------------------------')
    
    time_encode = time.time()
    
    for fname in os.listdir(DIR_INPUT) :
        fname_prefix, _ = os.path.splitext(fname)
        src_path  = os.path.join(DIR_INPUT, fname)
        dst_path  = os.path.join(DIR_ENCODED, fname_prefix)
        command = ENCODE_CMD.format(src_path, dst_path)
        runCommand(command)
    
    time_encode = time.time() - time_encode
    
    printColor(33, ('encode time: %.5f s\n' % time_encode))
    
    
    printColor(33, '-------------------------- start to decode --------------------------')
    
    time_decode = time.time()
    
    for fname in os.listdir(DIR_ENCODED) :
        fname_prefix, _ = os.path.splitext(fname)
        src_path  = os.path.join(DIR_ENCODED, fname)
        dst_path  = os.path.join(DIR_DECODED, fname_prefix)
        command = DECODE_CMD.format(src_path, dst_path)
        runCommand(command)
    
    time_decode = time.time() - time_decode
    
    
    printColor(33, ('encode time: %.5f s' % time_encode))
    printColor(33, ('decode time: %.5f s' % time_decode))
    







