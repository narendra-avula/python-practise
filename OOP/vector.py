__author__ = 'narendra'


class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


v = Vector(5)
u = v + [5,3,10,-2,1]


print u
# print v
# v[1] = 23
# v[-1] = 45
# print v
# print v[4]
#
# u = v + v
# print u
# total = 0
# for entry in v:
#     total += entry
# print total