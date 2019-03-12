#!/bin/python3

import math
import os
import random
import re
import sys
import argparse


argument_parser=argparse.ArgumentParser()
argument_parser.add_argument("intInput",help"-  intger input is required.")
arguments= argument_parser.parse_args()

if __name__ == '__main__':
    n = arguments.intInput

    arr = list(map(int, input().rstrip().split()))
    print(" ".join(map(str, arr[::-1])))
