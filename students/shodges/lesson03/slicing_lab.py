#!/usr/bin/env python

test_string = "This is a string."
test_tuple = (1,2,3,5,8,13)

def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]

assert exchange_first_last(test_string) == ".his is a stringT"
assert exchange_first_last(test_tuple) == (13,2,3,5,8,1)

def remove_every_other(seq):
    return seq[::2]

assert remove_every_other(test_string) == "Ti sasrn."
assert remove_every_other(test_tuple) == (1,3,8)

def ditch_outer_fours_every_other(seq):
    return seq[4:-4:2]

assert ditch_outer_fours_every_other(test_string) == " sasr"
assert ditch_outer_fours_every_other(test_tuple) == ()

def reverse(seq):
    return seq[::-1]

assert reverse(test_string) == ".gnirts a si sihT"
assert reverse(test_tuple) == (13,8,5,3,2,1)
