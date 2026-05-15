from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            currmin = self.stack[-1][1]
            if val<currmin:
                currmin = val
            self.stack.append((val,currmin))

        

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