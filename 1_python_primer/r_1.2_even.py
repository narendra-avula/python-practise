__author__ = 'narendra'

'''

Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.

'''
def is_even(n):
    print(True if (-1)**n==1 else False)

def using_bitwise(n):
    if n & 1 == 0:
        print True
    else:
        print False


# is_even(10)
using_bitwise(16)