#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

cache = {}
def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    max_cycle = 0

    if i > j:
        i, j = j, i

    for n in range(i, j+1):
        cycle_length = 1

        if n in cache:
            cycle_length = cache[n]
        else: 
            original_n = n
            while n != 1:
                if n%2 == 0:
                    n = n/2
                    cycle_length += 1
                elif n%2 == 1:
                    n = 3*n + 1
                    cycle_length += 1
            cache[original_n] = cycle_length
        if cycle_length > max_cycle:
            max_cycle = cycle_length
            
    return max_cycle
# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
