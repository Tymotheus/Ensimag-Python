#!/usr/bin/env python3
"""
Programme for detecting the longest subsequences
"""
import sys

#All those functions below are generator functions
def iter_number(file):
    """
    iterates over numbers in a file
    """
    #we are advised to use "split" function
    #so we will do
    x = file.read().split()
    for number in x:
        yield int(number)

def iter_subseq(file):
    """
    iterates over monotonous subsequences
    """
    #to do: border cases like 0 elements, 1 element

    generator = iter_number(file)
    is_increasing = None
    subseq = []
    #initialising first 2 numbers
    last_number = next(generator)
    current_number = next(generator)
    subseq.append(last_number)

    #skipping over first numbers if they are equal
    while( current_number == last_number):
        subseq.append(current_number)
        last_number = current_number
        current_number = next(generator)

    if(current_number>last_number):
        is_increasing = True
    else:
        is_increasing = False

    subseq.append(current_number)
    #now, we have a clear situation with monotonicity of our sequence

    for number in generator:
        last_number = current_number
        current_number = number
        if(is_increasing):
            if(current_number >= last_number):
                subseq.append(current_number)
                continue
            else:
                yield subseq
                subseq = [ subseq[-1] ]
                subseq.append(current_number)
                is_increasing = False
        else:
            if(current_number <= last_number):
                subseq.append(current_number)
                continue
            else:
                yield subseq
                subseq = [ subseq[-1] ]
                subseq.append(current_number)
                is_increasing = True

    yield(subseq)

def max(file):
    """
    returns the longest monotonous subsequences
    """
    max_size = 0
    sequence = []
    for subseq in iter_subseq(file):
        if len(subseq) > max_size:
            max_size = len(subseq)
            sequence = subseq
    return sequence

def main():
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Utilisation:", sys.argv[0], " filename_for_input")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        print(max(f))

main()
