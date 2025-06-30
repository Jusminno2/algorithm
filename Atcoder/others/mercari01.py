#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMinOperations(arr):
    # Write your code here
    n = len(arr)
    MAX_BIT = 31    # 10^9 < 2^30 < 2^31

    bit_count = [0] * MAX_BIT

    # 各ビットの1の個数を取得
    for val in arr:
        for b in range(MAX_BIT):
            if val >> b & 1:
                bit_count[b] += 1

    # 各ビットで必要な反転数を計算
    ops = 0
    for ones in bit_count:
        zeros = n - ones
        ops += min(ones, zeros)

    return ops


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMinOperations(arr)

    fptr.write(str(result) + '\n')

    fptr.close()