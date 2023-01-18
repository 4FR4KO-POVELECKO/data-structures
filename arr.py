import ctypes


class Array:
    def __init__(self):
        self.n = 0
        self.cap = 1
        self._a = self._make_array(self.cap)

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


if __name__ == "__main__":
    array = Array()
    array.append(1)
    print(array.cap)
    array.append(2)
    array.append(3)
    print(array)
    print(len(array))
    print(array.cap)
