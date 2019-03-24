# Author: Esteves (estti379) Tiago
# Date: 24/3/2019


# Origin: https://github.com/ati-ozgur/kurs-neural-networks-deep-learning/blob/master/python-introduction.md

# Question 02
#
# number_list = [1,2,3,...,100]
#
# There are 100 numbers in the variable number_list.
# Some of the numbers are unique in this list while some of the numbers exists more than one in this list.
# Find the non-unique ones.


import random
import sys

HIGHEST_NUMBER = 50
LOWEST_NUMBER = 0
NB_ELEMENTS = 100

# Not setting a seed, by default, system time is used as seed
# random.seed(379)

# Trow errors and quit when Constants have invalid values
if HIGHEST_NUMBER < LOWEST_NUMBER:
    sys.exit('Error: LOWEST_NUMBER is bigger than HIGHEST_NUMBER')
if NB_ELEMENTS < 2:
    sys.exit('Error: NB_ELEMENTS needs to be 2 or more')


# Preparation of list filled with random numbers
myNumbers = []

for i in range(NB_ELEMENTS):
    myNumbers.append(random.randint(LOWEST_NUMBER, HIGHEST_NUMBER))


# Search for duplicates and save a copy of them in "duplicates"
duplicates = []

for i in range(LOWEST_NUMBER, HIGHEST_NUMBER + 1):
    if myNumbers.count(i) > 1:
        duplicates.append(i)

print(duplicates)
