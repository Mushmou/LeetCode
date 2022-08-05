import collections
class MinStack:
    def __init__(self):
        self.stack = collections.deque()
        
    def push(self, val: int) -> None:
        #If its empty
        if len(self.stack) == 0:
            self.stack.append( (val, val))
        else:
            if val < self.stack[-1][1]:
                self.stack.append( (val, val)) 
            else:
                self.stack.append( (val, self.stack[-1][1]))
            
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()