'''
U 

[]

M
P
I
R
E
'''

import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        
        nums.sort()
        stack = collections.deque()
        for item in nums:
            if item not in stack:
                stack.append(item)
            else:
                stack.pop()
        return(stack[0])