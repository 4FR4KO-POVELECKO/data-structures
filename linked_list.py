from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        self._old_head = self.head
        return self

    def __next__(self):
        if self.head:
            x = self.head
            self.head = self.head.next
            return x.data
        self.head = self._old_head
        raise StopIteration

    def search(self, data):
        last = self.head
        index = 0
        while last:
            if last.data == data:
                return index
            last = last.next
            index += 1
        return None

    def get(self, idx):
        last = self.head
        index = 0
        while last:
            if index == idx:
                return last.data
            last = last.next
            index += 1
        raise IndexError('list index out of range')

    def add(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new

    def remove(self, idx):
        current = self.head
        last = None
        index = 0
        while current:
            if index == idx:
                if current is self.head:
                    self.head = current.next
                    del current
                    return True
                last.next = current.next
                del current
                return True
            last = current
            current = current.next
            index += 1
        raise IndexError('list index out of range') 

    def __str__(self):
        last = self.head
        if not self.head:
            return '[]'
        result = '['
        while last:
            result += f'{last.data}, '
            last = last.next
        return result[:-2] + ']' 
