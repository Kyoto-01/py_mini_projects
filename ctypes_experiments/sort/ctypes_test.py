#!/usr/bin/env python3

from ctypes import *


NUM_COUNT = 100000

numbers = (c_int * NUM_COUNT)()


def load_numbers():

    with open("input.txt", "r") as file:

        i = 0

        while (i < NUM_COUNT) and (n := file.readline()):

            numbers[i] = int(n)
            i += 1


load_numbers()

sortlib = CDLL("./sort.so")

sortlib.argtypes = [POINTER(c_int), c_int]

sortlib.bubbleSort(numbers, NUM_COUNT)