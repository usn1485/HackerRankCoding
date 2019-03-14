
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    Num_to_binary=bin(n)
    
    binary_num=Num_to_binary[2:].split('0')
    
    max_ones=max(binary_num)
    print(len(max_ones))