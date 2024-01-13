GraLIC lossless image compressor, ver. 1.11.demo
(C) 2009-2011, Alexander Ratushnyak, Graystone Compression Technologies Inc.

This executable is for 8-bit or 24-bit images with both width and height <=8160
Please feel free to email pqr@rogers.com and bfrusina@rogers.com for more info.

To compress|decompress a PNM file: Gralic111d.exe c|d archive file

Examples:
Gralic111d.exe c example.gra111 example.ppm
Gralic111d.exe d example.gra111 example2.ppm

--
This WIN32 executable was compiled with GCC 3.4.5 (mingw-vista special r3):
gcc -O3 -ffast-math -march=pentiumpro -fomit-frame-pointer -s Gralic111*.c -o Gralic111d.exe
