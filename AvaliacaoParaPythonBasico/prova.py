import math
import os
import random
import re
import sys

def avg(*n):
    soma = 0
    for i in n:
        soma = soma + i
    avge = soma / len(n)
    return avge

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()