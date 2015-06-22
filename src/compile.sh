#!/usr/bash


# filter iq data:
gcc -o ave8iq test_input_2.c
cat ../data/lee_ride_16-13.iq.bin | ./a.out | less

# test conversion from short int to uchar
gcc test_short_to_char.c -o stc && ./stc
