__author__ = 'narendra'

'''

Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.

'''


def min_max(data):
    minimum = None
    maximum = 0
    for i in data:
        if not minimum:
            minimum = i
        elif maximum < minimum or maximum < i:
            maximum = i
    return minimum, maximum

x = [1,12,2,53,23,6,17]
print min_max(x)