#!/usr/bin/env python

# File: calculate.py
# Initial date: 4 Sept 2020
# Author: Margot Clyne

# School assignment: For Assignment #0 of class MCDB6440: Software Engineering for Scientists

# Description: Intro to using GitHub Classroom. Practice with creating and uploading files to github etc.
# This file imports funcitons div and add from math_lib.py

import sys
import math_lib as ml

## --- input parameters ---(from command line or shell script)
cmd = sys.argv[1] #command (can be 'add' or 'div')
a = float(sys.argv[2]) #numerical
b = float(sys.argv[3]) #numerical

## print statements:
print('input values are '+ str(a) + ' and ' + str(b))

## ---


if cmd == 'add':
    foo = ml.add(a,b)
    print('the sum is: '+ str(foo))

if cmd == 'div':
    foo = ml.div(a,b)
    print('first/second is: '+ str(foo))



