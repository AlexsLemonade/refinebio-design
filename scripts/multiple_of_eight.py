#!/usr/bin/python
import math
def print_closest_multiples_of_eight(num):
    multipler = num/8
    previous_multiple = 8 * math.floor(multipler)
    next_multiple = 8 * (math.floor(multipler) + 1)
    print("previous_multiple " + str(previous_multiple))
    print("next_multiple " + str(next_multiple))
    return

while True:
    input_num = input("\n What's the number?  ")
    num = int(input_num)
    print_closest_multiples_of_eight(num)
