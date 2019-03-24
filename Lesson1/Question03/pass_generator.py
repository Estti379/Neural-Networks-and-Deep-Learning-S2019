# Author: Esteves (estti379) Tiago
# Date: 24/3/2019


# Origin: https://github.com/ati-ozgur/kurs-neural-networks-deep-learning/blob/master/python-introduction.md

# Question 03
#
# Write a simple program that creates 1000 Random passwords for users.


import random

# Not setting a seed, by default, system time is used
# random.seed(379)

for i in range(100): # generating 100 passwords
    nextPass = ''
    length = random.randint(8, 16) # choose nextPassword length
    for j in range(length):
        # range 33 to 126 are the only acceptable characters
        nextPass = nextPass + chr(random.randint(33, 126))
    print(nextPass)
