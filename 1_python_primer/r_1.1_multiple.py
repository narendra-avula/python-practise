__author__ = 'narendra'

'''

Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.

'''

def is_multiple(n, m):
    """ Checks if n is a factor of m where n <= m """
    try:
        if m%n == 0:
            print "Yes! {0} is a factor of {1}".format(n,m)
        else:
            print("Nope! {0} is NOT a factor of {1}".format(n,m))
    except Exception as e:
        print 'Error', e

is_multiple(10,50)