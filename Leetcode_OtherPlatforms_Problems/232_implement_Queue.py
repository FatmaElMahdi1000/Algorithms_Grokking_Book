class MyQueue(object):
    def __init__(self):
        self.queue = []
        
    def push(self, x):
        if not isinstance(x, int) :
            return "ERROR input"
        elif 1 <= x <= 9:
            self.queue.append(x)
        return(self.queue)

    def pop(self):
        if not self.queue:
            return "Error: Nothing to Pop, remove from the front"
        else:
            Removed_element = self.queue[0]
            self.queue.remove(Removed_element)
        return Removed_element
            
    def peek(self): #view the top item #Front in queue view the first item.
        if not self.queue:
            return "Error: Nothing to display"
        else:
            first_element = self.queue[0]
            return first_element
            
    def empty(self):
        if not self.queue:
            return True
        else:
            return False 
        
obj = MyQueue()
print(obj.push(2))
print(obj.push(3))
print(obj.push(7))
print(obj.pop())
print(obj.peek())
print(obj.empty())
