from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if (char == ')' and temp == '(') or (char == '}' and temp == '{') or (char == ']' and temp == '['):
                    continue
                else:
                    return False
        if len(stack)>0:
            return False
        else:
            return True
        
        







        