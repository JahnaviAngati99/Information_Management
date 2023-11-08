#!/usr/bin/env python3

import sys

def reducer():
    current_word = None
    current_count = 0

    for line in sys.stdin:
        # parse the input from mapper.py
        word, count = line.strip().split('\t', 1)
        # convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            continue

        # this IF-switch only works because Hadoop sorts map output
        if current_word == word:
            current_count += count
        else:
            if current_word:
                # write result to STDOUT
                print(f'{current_word}\t{current_count}')
            current_word = word
            current_count = count

    if current_word == word:
        print(f'{current_word}\t{current_count}')

if __name__ == '__main__':
    reducer()
