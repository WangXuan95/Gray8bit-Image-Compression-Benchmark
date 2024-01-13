# Gray 8-bit Lossless Image Compression benchmark

This repo provides scripts (Python) to run benchmark results of Gray 8-bit lossless image compression.

For benchmark data and results, see [Gray8 Lossless Photo Compression Benchmark](http://home.ustc.edu.cn/~wgg/gray8_LPCB.html) !!

　

## How to run benchmark

First, set several paths in [RunBenchmark.py][./RunBenchmark.py] : 

* `DIR_INPUT` is input directory. You need to put some .pgm grayscale 8-bit images inside it. For the format of .pgm file, see [PGM format specification](https://netpbm.sourceforge.net/doc/pgm.html)
* `DIR_ENCODED` is the directory to put the compressed images. Need to make it non-existent, the script will automatically create it.
* `DIR_DECODED` is the directory to put the uncompressed images. Need to make it non-existent, the script will automatically create it.

Then, uncomment one of the lines in [RunBenchmark.py][./RunBenchmark.py] to select a image codec.

- I've put the executable files of several codecs are in [codec](./codec) directory (include PNG, JPEG-XL, JPEG-LS, WEBP, BMF, Gralic, etc.). The script will use one of them to compress/decompress images.
- Note: I have attached the **copyright statements**, **licenses**, and **source from** of these codecs in the corresponding directory. If the original author wants me to supplement more statements, please contact me through the issue.

Then, just run the script in Windows:

```powershell
python RunBenchmark.py
```

　

## Benchmark data

For details on how to obtain large benchmark, please refer to [Gray8 Lossless Photo Compression Benchmark](http://home.ustc.edu.cn/~wgg/gray8_LPCB.html) !!

Here are only a few small images provided to test the scripts. [gray8_example](./gray8_example)

　　

## Additional instructions

### Using Python Pillow Library

Some codecs that run directly using Python Pillow library and its related libraries, and you can install them using pip.

```
python -m pip install pillow
python -m pip install pillow_jpls
```

I used Pillow 10.1.0 and pillow_jpls 1.3.2

　

### Run Linux binary

Some codecs are Linux binary which need to run on Linux. If your computer has Windows Subsystem of Linux (WSL) installed, you can also run them on Windows, as detailed in the comments in [RunBenchmark.py][./RunBenchmark.py] .

　

### Test Gray8 compression using RGB888 codecs

Some compressors only support RGB888 compression (including LEA, FLIC, QLIC2, HALIC, etc.).
To test them, I convert Gray8 images (.pgm) to RGB888 images (.ppm) as their input.
The method is: fill the original gray 8-bit channel to the RGB888's green channel, and set the red and blue channel to all zero.
I provide a Python Script to do it, just run:

```
python Gray2RGB.py <input-dir> <output-dir>
```

　

### Padding image width/height to multiple of 8

Since MRP only supports images that can be divided by 8 in length and width, I wrote a Python program to pad the image to a multiple of 8.

Just run:

```
python PadImage8.py <input-dir> <output-dir>
```

