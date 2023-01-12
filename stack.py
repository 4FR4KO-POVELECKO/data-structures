from node import Node


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def pop(self):
        last = self.head
        self.head = last.next
        del last

    def pip(self):
        last = self.head
        result = '['
        while last:
            result += f'{last.data}, '
            last = last.next
        return result[:-2] + ']'

    def __str__(self):
        return self.pip()


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pip())
    stack.pop()
    print(stack)
