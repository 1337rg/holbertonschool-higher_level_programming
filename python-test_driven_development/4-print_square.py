#!/usr/bin/python3


""" My module 1337rg """


def print_square(size):
    """ Method for print square """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print(size * '#')
