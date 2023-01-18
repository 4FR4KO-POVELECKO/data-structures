import unittest

from arr import Array


class TestDataStructures(unittest.TestCase):
    def test_array(self):
        arr = Array()
        
        arr.append(1)
        assert arr.cap == 1
        arr.append(2)
        assert arr.cap == 2
        arr.append(3)
        assert arr.cap == 4

        assert arr[0] == 1
        assert arr[1] == 2
        assert arr[2] == 3

        arr[0] = 100
        assert arr[0] == 100

        assert len(arr) == 3


if __name__ == '__main__':
    unittest.main()