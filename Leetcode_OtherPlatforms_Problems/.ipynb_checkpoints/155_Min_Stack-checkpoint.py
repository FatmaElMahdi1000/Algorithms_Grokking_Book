class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        if not isinstance(val, int):
            return "ERROR, Entered value is not an integer"
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        print(self.stack)
        
    def pop(self):
        if not self.stack:
            return "Error, stack is empty, nothing to pop"
        else:
            popped = self.stack.pop()
        print(self.stack)
        
    def top(self):
        if not self.stack:
            return "Error, stack is empty, nothing to display"
        else:
            topmost_number = self.stack[-1]
            print(self.stack[-1])
    def getMin(self):
        if not self.stack and not self.min_stack:
            return "Error, stack is empty, nothing to check"
        else:
            print(self.min_stack[-1])

obj = MinStack()
obj.push(5)
obj.push(6)
obj.push(6)
obj.pop()
obj.top()
obj.getMin()
obj.push(3)
obj.push(1)
obj.getMin()
obj.push(3)
obj.getMin()



#obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()