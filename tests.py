import unittest

from arr import Array
from linked_list import LinkedList
from que import Queue
from stack import Stack
from set import Set


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

    def test_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        assert queue.head.data == 1
        assert queue.head.next.data == 2
        queue.dequeue()
        assert queue.head.data == 2
        assert queue.head.next == None

    def test_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)

        assert stack.head.data == 2
        assert stack.head.next.data == 1
        stack.pop()
        assert stack.head.data == 1
        assert stack.head.next == None

    def test_set(self):
        a = Set()
        a.add(1)
        a.add(2)
        a.add(3)

        b = Set()
        b.add(3)
        b.add(4)
        b.add(5)
        
        assert all(x1 == x2 for x1, x2 in zip(a.union(b), [1, 2, 3, 4, 5]))
        assert all(x1 == x2 for x1, x2 in zip(a.intersection(b), [3]))
        assert all(x1 == x2 for x1, x2 in zip(a.difference(b), [1, 2]))
        assert all(x1 == x2 for x1, x2 in zip(b.difference(a), [4, 5]))
        assert a.subset(b) == False
        assert a.subset(a) == True


if __name__ == '__main__':
    unittest.main()
