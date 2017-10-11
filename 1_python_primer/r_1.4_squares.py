__author__ = 'narendra'

'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.

'''

def _sum_squares(n):
    squares = 0
    for i in range(n):
        squares += i*i
    return squares

print _sum_squares(18)


'''

Give a single command that computes the sum from Exercise R1.4, rely
ing on Pythons comprehension syntax and the built-in sum function.

'''

def _sum_squares_2(n):
    return sum(i*i for i in range(n))

print _sum_squares_2(18)


'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.

'''

def _sum_squares_3(n):
    return sum(i*i for i in range(n) if i%2!=0)

print _sum_squares_3(18)