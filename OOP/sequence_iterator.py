__author__ = 'narendra'


class SequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration

    def __iter__(self):
        return self


a = SequenceIterator([1,1,2,5,3,5])
print a.__next__()
print a.__next__()
print a.__next__()
print a.__next__()
print a.__next__()