from node import Node


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new

    def dequeue(self):
        last = self.head
        self.head = last.next
        del last

    def __str__(self):
        last = self.head
        result = '['
        while last:
            result += f'{last.data}, '
            last = last.next
        return result[:-2] + ']'
