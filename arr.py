import ctypes


class Array:
    def __init__(self):
        self.n = 0
        self.cap = 1
        self._a = self._make_array(self.cap)

    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self):
        if self.n != self._iter:
            next = self._a[self._iter]
            self._iter += 1
            return next
        raise StopIteration

    def __str__(self):
        if self.n == 0:
            return '[]'
        result = '['
        for i in range(self.n):
            result += f'{self._a[i]}, '
        return result[:-2] + ']'

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError('list index out of range')
        return self._a[index]

    def __setitem__(self, index, value):
        if not 0 <= index < self.n:
            raise IndexError('list index out of range')
        self._a[index] = value

    def append(self, value):
        if self.n == self.cap:
            self._resize(2*self.cap)
        self._a[self.n] = value
        self.n += 1

    def _resize(self, cap):
        b = self._make_array(cap)
        for i in range(self.n):
            b[i] = self._a[i]
        self._a = b
        self.cap = cap

    def _make_array(self, cap):
        return (cap * ctypes.py_object)()
