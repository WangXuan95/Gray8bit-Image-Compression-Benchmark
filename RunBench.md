# How to Run Benchmark

　

## Get Benchmark Images

The benchmark data set has 62 images totaling 751 MB, which is as same as the 62 images in <a href="http://qlic.altervista.org/">24-bit RGB LPCB</a>, but has converted to gray 8-bit.

Since the benchmark images are large, here I only provide a few small images in [gray8_example](./gray8_example) for you to test the scripts.

To get the benchmark images, you should download them as follow steps:

- First, download all the "Sample RAW Images" from the following four sites: <a href="http://www.photographyblog.com/reviews/olympus_xz1_review#sample_images">Olympus</a>, <a href="http://www.photographyblog.com/reviews/sony_a55_review#sample_images">Sony</a>, <a href="http://www.photographyblog.com/reviews/fujifilm_finepix_x100_review#sample_images">Fujifilm</a>, and <a href="http://www.photographyblog.com/reviews/canon_eos_1100d_review#sample_images">Canon</a>. <i>Please find the "Sample RAW Images" section on the webpage to download, instead of the "Sample Images" section.</i>
- After downloading, remove some similar images among them. On the <b>Sony</b> page images 12, 13, 14 were excluded as they are very similar to image 11, and for the same reason images 7, 8, 9, 10 from the <b>Canon</b> set, images 7, 8, 9 from the <b>Fujifilm</b> set.
- After removing, I keeps 62 images for testing, see the bottom of this webpage.
- Then, convert all the downloaded images to <b>24-bit RGB .ppm format</b> using <a href="https://www.xnview.com/en/nconvert/#downloads">NConvert 7.163</a>.
  The method is to run the following command in the directory where the image is located:

```powershell
nconvert.exe -out ppm -high_res -raw_camerabalance *.orf *.arw *.raf *.cr2
```

- Then, convert the images from <b>24-bit RGB .ppm format</b> to <b>8-bit grayscale .pgm format</b> using <a href="https://www.xnview.com/en/nconvert/#downloads">NConvert 7.163</a>. The method is to run the following command in the directory where the image is located:

```powershell
nconvert.exe -grey 256 -out pgm *.ppm
```

<i>Note: .pgm is a simple uncompressed 8-bit gray image format. Many compressors support .pgm format as input.</i> <i>For some compressors that dont support inputting .pgm (e.g., RKIM, WEBP), I use nconvert.exe to convert .pgm to the format they directly supported.</i>

　

## list of the 62 test images

```
name                         width x height
canon_eos_1100d_01            4290 x 2856
canon_eos_1100d_02            2856 x 4290
canon_eos_1100d_03            4290 x 2856
canon_eos_1100d_04            4290 x 2856
canon_eos_1100d_05            4290 x 2856
canon_eos_1100d_06            2856 x 4290
canon_eos_1100d_11            4290 x 2856
canon_eos_1100d_12            4290 x 2856
canon_eos_1100d_13            2856 x 4290
canon_eos_1100d_14            4290 x 2856
canon_eos_1100d_15            2856 x 4290
fujifilm_finepix_x100_01      4310 x 2870
fujifilm_finepix_x100_02      4310 x 2870
fujifilm_finepix_x100_03      2870 x 4310
fujifilm_finepix_x100_04      2870 x 4310
fujifilm_finepix_x100_05      2870 x 4310
fujifilm_finepix_x100_06      2870 x 4310
fujifilm_finepix_x100_10      4310 x 2870
fujifilm_finepix_x100_11      4310 x 2870
fujifilm_finepix_x100_12      4310 x 2870
fujifilm_finepix_x100_13      2870 x 4310
fujifilm_finepix_x100_14      4310 x 2870
fujifilm_finepix_x100_15      4310 x 2870
olympus_xz1_01                2760 x 3680
olympus_xz1_02                2760 x 3680
olympus_xz1_03                2760 x 3680
olympus_xz1_04                2760 x 3680
olympus_xz1_05                2760 x 3680
olympus_xz1_06                3680 x 2760
olympus_xz1_07                2760 x 3680
olympus_xz1_08                2760 x 3680
olympus_xz1_09                2760 x 3680
olympus_xz1_10                2760 x 3680
olympus_xz1_11                3680 x 2760
olympus_xz1_12                3680 x 2760
olympus_xz1_13                3680 x 2760
olympus_xz1_14                3680 x 2760
olympus_xz1_15                3680 x 2760
olympus_xz1_16                3680 x 2760
olympus_xz1_17                3680 x 2760
olympus_xz1_18                2760 x 3680
olympus_xz1_19                3680 x 2760
olympus_xz1_20                2760 x 3680
olympus_xz1_21                2760 x 3680
olympus_xz1_22                2760 x 3680
olympus_xz1_23                2760 x 3680
olympus_xz1_24                2760 x 3680
olympus_xz1_25                3680 x 2760
olympus_xz1_26                3680 x 2760
olympus_xz1_27                2760 x 3680
sony_a55_01                   4928 x 3280
sony_a55_02                   4928 x 3280
sony_a55_03                   4928 x 3280
sony_a55_04                   4928 x 3280
sony_a55_05                   4928 x 3280
sony_a55_06                   3280 x 4928
sony_a55_07                   4928 x 3280
sony_a55_08                   3280 x 4928
sony_a55_09                   4928 x 3280
sony_a55_10                   3280 x 4928
sony_a55_11                   4928 x 3280
sony_a55_15                   3280 x 4928
```

　

　

　

## Run Benchmark

**Step1**: config paths in [RunBenchmark.py](./RunBenchmark.py) : 

```python
DIR_INPUT   = 'gray8_example'   # Input directory. put some .pgm grayscale 8-bit images inside it. For the format of .pgm file, see https://netpbm.sourceforge.net/doc/pgm.html
DIR_ENCODED = 'encoded'         # Directory to put the compressed images.   Make it non-existent, this program will automatically create it.
DIR_DECODED = 'decoded'         # Directory to put the decompressed images. Make it non-existent, this program will automatically create it.
```

**Step2**: Uncomment one of the lines in [RunBenchmark.py](./RunBenchmark.py) to select a image codec. The script will call the executable files in [codec](./codec) directory to compress/decompress images.

Note: I've put several image codecs in [codec](./codec) directory, including **PNG**, **JPEG-XL**, **JPEG-LS**, **BMF**, **Gralic**, etc.. I also attach the **copyright statements**, **licenses**, and **source from** of these codecs in the corresponding directory. If the authors of the codecs want me to supplement more statements, please contact me through the issue.

**Step3**: run the script in Windows:

```powershell
python RunBenchmark.py
```

　

　

　

## Additional instructions

### Using Python Pillow Library

Some codecs that run directly using Python Pillow library and its related libraries, and you can install them using `pip`.

```
python -m pip install pillow
python -m pip install pillow_jpls        # for JPEG-LS
```

I used Pillow 10.1.0 and `pillow_jpls` 1.3.2

　

### Run Linux binary

Some codecs are Linux binary which need to run on Linux. If your computer has Windows Subsystem of Linux (WSL) installed, you can also run them on Windows, as detailed in the comments in [RunBenchmark.py](./RunBenchmark.py).

　

### Run Gray8 compression using RGB888 codecs

Some compressors only support RGB888 compression (including LEA, FLIC, QLIC2, HALIC, etc.).
To test them, I convert Gray8 images (.pgm) to RGB888 images (.ppm) as their input.
The method is: fill the original gray 8-bit channel to the RGB888's green channel, and set the red and blue channel to all zero.
I provide a Python Script to do it, just run:

```
python Gray2RGB.py <input-dir> <output-dir>
```

　

### Padding image width/height to multiple of 8

Since MRP only supports images that can be divided by 8 in length and width, I wrote a Python program to pad the image to a multiple of 8. Just run:

```
python PadImage8.py <input-dir> <output-dir>
```

