'''
Input tests

can the string be empty? No
can the string have only one item? Yes
can there be "{}" or "[]" No

iterate through the string

we care about "(" or ")"

test cases => 

t1 = "(()())""
     () = 1, ()=1 => 1+1 * 2 = 4
return 4

t2 = "()"
return 1

t3 = "( () (()) )" => 2 (1 + 2) = 6
return 6

Plan
t1 = "(()())""
stack = []

stack = [(, 1, 1]

if elem is ")"
    stack pop
    append(1)
else:
    stack.append(elem)
    

score = 0
while len(stack) != 0:
    if stack peek equals 1:
        score += 1
    else:
        score = score * 2
    stack.pop
'''
from collections import deque
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if len(s) == 2:
            if s[0] == "(" and s[1] == ")":
                return 1
        stack = deque()
        score = 0
        result = 0
        
        for elem in range(0, len(s)):
            if s[elem] == "(":
                stack.append(0)
            else:
                mul = stack.pop()
                if mul == 0:
                    score = 1
                else:
                    score = mul * 2
                    
                if len(stack) == 0:
                    result += score
                else:
                    stack[-1] += score
        return result

                    
                
            
 