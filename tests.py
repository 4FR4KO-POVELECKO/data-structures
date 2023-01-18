import unittest

from arr import Array
from linked_list import LinkedList


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

    def test_linked_list(self):
        linked_list = LinkedList()
        
        linked_list.add(1)
        linked_list.add(2)
        assert linked_list.get(0) == 1
        assert linked_list.get(1) == 2
        
        assert linked_list.search(1) == 0
        assert linked_list.search(100) is None

        linked_list.remove(0)
        assert linked_list.get(0) == 2


if __name__ == '__main__':
    unittest.main()
