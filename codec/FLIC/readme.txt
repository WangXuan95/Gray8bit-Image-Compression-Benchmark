FLIC - fast lossless image compressor, version 2.1.demo
(c) 2010-2011, Alexander Ratushnyak, Graystone Compression Technologies Inc.

To compress|decompress a PPM file:  FLIC.exe c|d archive file
Examples:
FLIC.exe c example.flic21 example.ppm
FLIC.exe d example.flic21 example_decompressed.ppm

Both executables are for 24-bit images with both width and height <=8184.

Please feel free to email pqr@rogers.com and bfrusina@rogers.com for more info.
You can post comments here:
http://www.linkedin.com/groups/FLIC-fast-lossless-image-compressor-3363256.S.42748372

The 32-bit Windows executable was compiled with GCC 3.4.5 (mingw-vista special r3):
gcc FLIC.c -O4 -ffast-math -march=pentiumpro -fomit-frame-pointer -s -o FLIC.exe
The 64-bit Windows executable was compiled with GCC 4.7.0 20110827 (experimental):
gcc FLIC64.c -O4 -ffast-math -march=native -fomit-frame-pointer -s -o FLIC64.exe
No CPU-specific optimizations, no profiling data usage.
