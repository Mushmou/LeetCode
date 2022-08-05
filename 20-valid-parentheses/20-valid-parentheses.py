import collections
class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        characters = {")":"(", "}":"{", "]":"["}
        
        if s[0] in characters or len(s) % 2 == 1:
            return False
        
        for item in s:
            if item in characters.keys():
                if len(stack) != 0 and characters[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
            
        print("--------------------------")
        if len(stack) == 0:
            return True
