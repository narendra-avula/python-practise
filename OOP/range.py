__author__ = 'narendra'

# r = range(8,140,0)
# print r
# print len(r)
# print r.__len__()
# print r.__getitem__(2)
#
#
# start = 8
# stop = 140
# step = 5
#
# print max(0, (stop-start+step-1)//step)

class Range:

    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('range() step argument must not be zero')

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop-start+step-1)//step)
        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        if item < 0:
            item += len(self)

        if not 0 <= item < self._length:
            raise IndexError('Index out of range')

        return self._start + item * self._step


a = Range(0,stop=None)
print a