'''
happy case

Are there duplicates? 
Can numbers be negative?
Can the input be empty?
What about 1 item?

What is the target time complexity? Space Complexity?

nums = [-5,-1,2, 20, 5]
result = 2

nums = [0,0,0,0,1,2,4,2,1]
result = 2

nums = []
result = 0

nums = [0]
result = 1
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        print(f'working with {nums}')
        length = 0
        distance = 1
        
        for current in range(1, len(nums)):
            previous = nums[current-1]
            
            if (nums[current] - previous) == 1:
                distance += 1
            elif nums[current] == previous:
                distance = distance
            else:
                distance = 1
            length = max(length,distance)
        return length