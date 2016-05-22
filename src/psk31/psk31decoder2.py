#!/usr/bin/env python

import re
import struct
import varicode
import psk31decoder

psk31decoder.psk31_demod().run()

# TODO: Make the .raw file a variable
infile = open("output.raw", mode='rb')

# Initialize the loop
sample_cnt = 0
prev_bit = '0'
bit_stream = ''

# Loop through, sampling 176 samples after each transition
# or after 352 samples if there was no transition.
curr_bit = infile.read(1)
while curr_bit != "":
    curr_bit = infile.read(1)
    if (prev_bit != curr_bit):
        sample_cnt = 0
    else:
        sample_cnt += 1
        if ((sample_cnt - 176) % 352) == 0:
            bit_stream = bit_stream+str(struct.unpack('B', curr_bit)[0])

    prev_bit = curr_bit

# This prints the bit stream
# print "Bit Stream: ", bit_stream

# Use regular expression to separate the characters
# by splitting on two or more 0s
char_list = re.split('00+', bit_stream)

# This prints out the character list that re splits with 2 or more "0"
# i.e. 00 or 0000 or 000 will split the string.
# this is then put into a list called char_list

# print "Character List: ", char_list

# Use the dictionary to decode the characters
output_str = ''
for char in char_list:
    if char in varicode.decode:
        output_str = output_str+varicode.decode[char]

f = open('MESSAGE', 'w')
f.write(output_str)

