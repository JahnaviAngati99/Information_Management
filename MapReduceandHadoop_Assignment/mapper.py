#!/usr/bin/env python3

import sys
import re

def mapper():
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        words = re.findall(r'\w+', line)
        # output each word as a key-value pair
        for word in words:
            print(f'{word}\t1')

if __name__ == '__main__':
    mapper()
