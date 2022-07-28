'''
Understand

Happy Cases
nums = [-2,3,-1,2]
output => [-2,3,-1]

# Edge Cases
nums = [0,1,1], output => []
nums = [0,0,0], output => [0,0,0]

           r
         l
nums = [-2,3,-1,2]
nums = [-1,0,1,2,-1,-4]

Plan

Review

Evaluate
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            
        nums = sorted(nums)
        # print(f'sorted {nums}')
        
        result = []
        for i in range(len(nums)):
            #skip duplicates by checking prev and current, if they are same continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # print(nums[i])
            left = i+1
            right = len(nums)-1
            
            while left < right:
                # print(f'nums {nums[i]} left {nums[left]} right {nums[right]} output {nums[i] + nums[left] + nums[right]}')
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    listSum = [nums[i], nums[left], nums[right]]
                    if listSum not in result:
                        result.append(listSum)
                    left += 1
        return(result)
