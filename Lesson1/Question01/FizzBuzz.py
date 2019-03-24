# Author: Esteves (estti379) Tiago
# Date: 24/3/2019


# Origin: https://github.com/ati-ozgur/kurs-neural-networks-deep-learning/blob/master/python-introduction.md

# Question01: FizzBuzz A Very Well Known Interview Question
#
# Write a program that prints the numbers from 1 to 100. If it’s a multiple of 3, it should print “three”.
# If it’s a multiple of 5, it should print “five”. If it’s a multiple of 3 and 5, it should print "fifteen”.


for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print(f'{i} : fifteen')
        else :
            print(f'{i} : three')
    elif i % 5 == 0:
        print(f'{i} : five')
    else:
        print(f'{i} :')


