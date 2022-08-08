class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] != (nums[i-1]+1):
                return nums[i-1]+1
        
        if len(nums) == nums[-1]:
            return 0
        return nums[-1] + 1
