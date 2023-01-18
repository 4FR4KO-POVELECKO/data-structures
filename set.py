from arr import Array


class Set(Array):
    def add(self, data):
        if data in self:
            return
        self.append(data)
    
    def union(self, other):
        new = Set()
        for i in self:
            new.add(i)
        for i in other:
            new.add(i)

        return new

    def intersection(self, other):
        new = Set()
        for i in self:
            if i in other:
                new.add(i)
        return new
    
    def difference(self, other):
        new = Set()
        for i in self:
            if i not in other:
                new.add(i)
        return new

    def subset(self, other):
        return True if not self.difference(other) else False
