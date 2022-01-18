class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        # for i in range(len(nums)):
        #     prev = nums[i]
        #     if nums[i+1] < nums[i]:
        #         return nums[i+1]
        # return nums[0]
        i,j = 0,1
        while i < len(nums) and j < len(nums):
            if nums[j] < nums[i]: return nums[i+1]
            i+=1
            j+=1
        return nums[0]