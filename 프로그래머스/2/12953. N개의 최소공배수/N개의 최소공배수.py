from math import *
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    arr_gcd = reduce(gcd, arr)
    return reduce(lcm, arr)