class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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

    def __str__(self):
        last = self.head
        result = '['
        while last:
            result += f'{last.data}, '
            last = last.next
        return result[:-2] + ']' 


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    print('Index: 0 Data: ', linked_list.get(0))
    print('Data: 1 Index: ', linked_list.search(1))
    print('Data: 0 Index: ', linked_list.search(0))
    print(linked_list)

