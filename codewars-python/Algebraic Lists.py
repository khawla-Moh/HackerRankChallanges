class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
      
    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])
      
    @classmethod
    def from_array(cls, arr):
        #TODO: convert a Python list to an algebraic list.
        pass
    
    def filter(self, fn):
        #TODO: construct new algebraic list containing only elements
        #      that satisfy the predicate.
        pass
    
    def map(self, fn):
        #TODO: construct a new algebraic list containing all elements
        #      resulting from applying the mapper function to a list.
        pass

numbers = Cons(1, Cons(2, Cons(3, Cons(4, Cons(5, None)))))
print(numbers)