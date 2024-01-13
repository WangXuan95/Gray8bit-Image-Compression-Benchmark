            1. Short DESCRIPTION.
    BMF  program  is  lossless/near-lossless  image  compression  utility.  It
supports true colour, high colour, greyscale and paletted images  compression.
Compressed  images  are  stored  in  own  BMF  file  format which is naturally
incompatible  with  any  other  image  file  format.  BMF  program  is  "image
compressor", but not "archiver", so it warrants (in lossless mode)  bit-by-bit
equality of incoming and decompressed  images, but not bit-by-bit equality  of
incoming and decompressed  files.  In  other words, BMF  file format is  image
format, like to  GIF(sm), PNG or  TIFF, but not  archiver format like  to ZIP,
RAR etc. You can  expect 10-50% storage saving,  when You converts GIF  or PNG
files to BMF files.

            2. Distribution CONTENTS.
    read_me.txt  - this file;
    bmf_vers.txt - description of differences between versions;
    TestFile.bmf - test image;
    BMFViewW.exe - simple BMF file viewer;
    BMF.ini      - example of configuration file;
    BMF.exe      - main program converts TGA, BMP, RAS, GIF, PNM and RAW
image files to BMF files and BMF files to TGA, BMP, PNM or RAW image files;

            3. Usage NOTES.
    1.   Program  uses  SSE  floating  point,  so  it  will  not  run on older
processors;
    2. Wildcards are allowed.
    3. BMF file format supports many images in one file.
    4. Raw images are interpreted in next manner: 8bpp - greyscale image,
16bpp - highcolor one, 24bpp - BGR one, 32bpp - BGRA one.
    5. Some programs does  not understand 1-, 2-,  4-bit TGA images, so  these
images stored the same as 8-bit images;
    6. Command line for tightest compression:
BMF -q9 [-s] *.bmp
    7. Command line for fastest decompression:
BMF -n -tga *.bmf
    8.  Command  line  for  fastest  compression of line-drawings and paletted
images:
BMF -f- [-s] *.bmp
    9. Effects of -qX option.
Test image set: 169 truecolour images with total size ~410MB.
               Fast mode                         Slow mode
-qX       Total    ETime    DTime           Total    ETime    DTime
  0   152509000    68.88    36.20       129378440  1341.95  1169.31
  1   152287312    77.88    36.19       128402996  1441.75  1128.61
  2   151501276    88.65    36.16       128372980  1568.45  1122.18
  3   151231752   103.04    36.20       128342492  1725.61  1110.15
  4   151183112   119.90    36.31       128176268  1976.89  1144.64
  5   151074616   140.33    36.25       128171224  2188.74  1142.28
  6   151016228   162.20    36.19       128171876  2409.47  1142.18
  7   151255528   187.40    35.92       128030284  2606.61  1139.32
  8   150255484   252.16    35.48       128027596  2791.26  1141.79
  9   150225436   369.26    35.32       127962968  3612.20  1141.07

    10. Image filters  selection is time  consuming operation, so, if You have
large sequence  of similar  images, You  can store  filters configuration  for
first  image  with  '-t1'  option  and  use  stored  value  for compression of
following images with '-t2'  option. All not-retouched greyscale  photographic
images  are  always  compressed  with   the  same  filter.   Demonstation   of
compression  speedup  with  '-t'  option   for  test  image  set  (UCID v.2.0)
consisting  of  1338  truecolour  photographic  images with total size ~789MB,
filters were selected for first image (ucid00001.bmp):
BMF -t0 *.bmp        - 394264748 bytes,  215.69 sec.
BMF -t2 *.bmp        - 394182996 bytes,  144.40 sec.
BMF -t0 -q9 *.bmp    - 393428724 bytes,  717.37 sec.
BMF -t2 -q9 *.bmp    - 394041688 bytes,  209.10 sec.
BMF -t0 -s *.bmp     - 358264156 bytes, 5504.50 sec.
BMF -t2 -s *.bmp     - 358248708 bytes, 4217.19 sec.
BMF -t0 -s -q9 *.bmp - 358235272 bytes, 9655.20 sec.
BMF -t2 -s -q9 *.bmp - 358248636 bytes, 4416.02 sec.

    11. Near-lossless  compression is  more accurate  and controllable against
JPEG-like technique, every  colour sample of  decompressed image is  guaranted
to differ from  corresponding sample of  original image by  up to user-defined
error. Error values  <= 3 provide  visually lossless compression  for the most
of images. It  is not recommended  to use errors  larger than 5,  there exists
better methods for such  big errors.  Paletted  and high colour images  can be
compressed losslessly only, You can use near-lossless mode in conjuction  with
arhiving mode(/ra) at your own risk.
    12. BMFViewW program treats 16-bit highcolor images as 15-bit ones (is  it
common practice?).
    13. Windows Explorer configuration for BMFViewW:
    Run Explorer.exe
    Goto View->Options->File Types
    Make a new type, called "BMF Image"
    Set its MIME type to "image/bmf"
    Set the default extension to ".bmf"
    Set the          "&Open" command to: ProgramPath\BMFViewW.exe O
    Set the          "&Clip" command to: ProgramPath\BMFViewW.exe C
    Set the "&Extract to..." command to: ProgramPath\BMFViewW.exe E
    Leave DDE checkbox unchecked
    Close all dialogs and double-click on TestFile.bmf, test image(diagram)
must be showed

            4. As any program, this one has LIMITATIONS.
    GIF & TGA file format extensions are skipped during processing;
    TGA file format implementation supports 24-bit palettes only;
    BMP file  format implementation  corresponds Windows  3.0 BMP  file format
specification;
    BMP  file  palette  alpha-channel(rgbReserved  field)  is  skipped  during
processing;
    RAS file format implementation  supports 0, 1, 2,  3 image types only  and
it does not supports RMT_RAW MapType;
    PNM files with comments disturb standard specification for PNM format  and
such files are not supported;
    Memory  requirements   for  current   implementation  are   2*ImageSize  +
3*ColourPlaneSize  for  compression,  and  ImageSize  +  CompressedImageSize +
ColourPlaneSize for decompression;

            5. When to MAIL.
    If You found bugs (they exists, no doubt), send me mail!  In general,  all
remarks and suggestions are  welcome.

    AUTHOR SHALL NOT BE LIABLE FOR ANY DIRECT, INDIRECT, SPECIAL,  INCIDENTAL,
OR CONSEQUENTIAL  DAMAGES ARISING  OUT OF  ANY USE  OF THIS  SOFTWARE. YOU USE
THIS PROGRAM AT YOUR OWN RISK.
    PERMISSION  IS  GRANTED  FOR  PERSONAL  USE  AND  RESEARCH  OR COMPARATIVE
PURPOSES ONLY, NOT FOR COMMERCIAL USE.   YOU CAN REDISTRIBUTE THIS PACKAGE  TO
OTHER  PERSONS  FREELY  (IN  TERMS  OF  THIS AGREEMENT) WITHOUT ANY CHANGES OR
ADDITIONS.

                                        Dancy compression!
                                        Dmitry Shkarin
                                        E-mail: dmitry.shkarin@mtu-net.ru
