gcc -O4 -funroll-loops -lm -Wall -o mrp_enc.exe src\encmrp.c src\common.c src\rc.c
gcc -O4 -funroll-loops -lm -Wall -o mrp_dec.exe src\decmrp.c src\common.c src\rc.c