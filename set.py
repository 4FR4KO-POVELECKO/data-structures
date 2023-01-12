from linked_list import LinkedList


class Set(LinkedList):
    def add(self, data):
        if self.search(data):
            return
        super().add(data)
    
    def union(self, other):
        new = Set()
        first = self.head
        while first:
            new.add(first.data)
            first = first.next
        second = other.head
        while second:
            new.add(second.data)
            second = second.next
        
        return new

    def intersection(self, other):
        new = Set()
        first = self.head
        while first:
            if other.search(first.data) is not None:
                new.add(first.data)
            first = first.next
        return new
    
    def difference(self, other):
        new = Set()
        first = self.head
        while first:
            if other.search(first.data) is None:
                new.add(first.data)
            first = first.next
        return new

    def subset(self, other):
        return True if not self.difference(other).head else False


if __name__ == '__main__':
    a = Set()
    a.add(1)
    a.add(2)
    a.add(3)
    print(a)

    b = Set()
    b.add(3)
    b.add(4)
    b.add(5)
    print(b)

    print(a.union(b))
    print(a.intersection(b))
    print(a.difference(b))
    print(b.difference(a))
    print(a.subset(b))
    print(a.subset(a))
