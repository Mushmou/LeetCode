'''
Understand

#Last element is always a 0

Happy Cases
[54, 66, 31, 31, 31, 70]
result = 1, 4, 3, 2, 1, 0

Edge Cases
[30]
result = 0

[31,31,31,31]
result = 0,0,0,0

Match
Two Pointer
Double loop

Plan
result = [1, 4, 3, 2, 1, 0]
distance = 0

 c   r                                 
[54, 66, 31, 31, 31, 70]

Implement

Review

Evaluate

'''
import collections
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        
        result = [0]*len(temperatures)
        stack = collections.deque()
        
        for i in range(len(temperatures)):
            # print(result, stack)
            while len(stack) != 0:
                if temperatures[i] > stack[-1][1]:
                    top = stack.pop()
                    index = top[0]
                    curr_index = i

                    distance = curr_index - index
                    result[index] = distance
                else:
                    break
            stack.append( (i, temperatures[i]) )
        
        
        for i, item in stack:
            result[i] = 0
        return result
        