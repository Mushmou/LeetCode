'''
Understand
# What happens if the input is empty?
# What happens if the input has one item?

General

area = base * height
height = [1,8,6,2,5,6,8,3,7]
output = 49

height = [1, 4, 3]
output = 3

height = []
output = 0

height = [1,2]
output = 1


Match
Two pointer approach
max function

Plan
area = base * height
- we always want to use the minimum height
- base = right - left

area = 49
area = 0
          0 1 2 3 4 5 6 7 8
            l r     
height = [1,8,6,2,5,4,8,3,7]

            l         r
height = [1,8,6,2,5,4,8,3,7

Solution 1

initialize left pointer, right pointer

iterate through the heights, with right pointer

if right pointer > left pointer:
    move left pointer to right pointer

calculate area
max (area, maxArea)

Implement

Review

Evaluate
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
        left = 0
        right = len(height)-1
        result = 0
        while left < right:
            area = min (height[left], height[right]) * (right - left)
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result