import collections
class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        characters = {")":"(", "}":"{", "]":"["}
        if len(s) % 2 == 1:
            return False
        for item in s:
            if item in characters.keys():
                if len(stack) != 0 and characters[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
                
        if len(stack) == 0:
            return True
