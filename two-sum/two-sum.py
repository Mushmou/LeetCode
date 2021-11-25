class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for x in range(i+1, len(nums)):
                sum = nums[i] + nums[x]
                if sum == target:
                    return [i,x]
        