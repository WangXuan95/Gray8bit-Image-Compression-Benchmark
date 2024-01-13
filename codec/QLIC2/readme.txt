QLIC - quick lossless image compressor, ver. 2.demo
(c) Alexander Rhatushnyak

Please feel free to send an email to qlic@live.com for more info.

To compress|decompress a PPM file: QLIC.exe c|d archive file
Examples:
QLIC.exe c example.qlic2 example.ppm
QLIC.exe d example.qlic2 example_decompressed.ppm

The 2.demo executable is

1. for 24-bit images
2. with both width and height <=32768
3. it does not check whether output is smaller or bigger than input.

The 32-bit Windows executable was compiled with MinGW 4.8.1
with no profiling data usage, and no assembly instructions in the source code.




Version 2 of QLIC applies ideas from rANS, tANS and FSE.
rANS and tANS are in public domain, while FSE requires this:


Copyright (c) 2013, Yann Collet
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.