'''
Understand
[0,1,0,3,12]
[1,3,12,0,0]

[0]
[0]

[-2, -4, 0 , 3, 0, 12]
[-2, -4, 3, 12 , 0, 0]


Match
Two Pointer Approach

Plan

Implement
Review
Evaluate
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # result = [0] * len(nums)
        # i = 0
        # for num in nums:
        #     if num != 0:
        #         result[i] = num
        #         i+=1
        # nums = result.copy()
        
        # l = 0
        # while l <= len(nums)-1:
        #     r = l+1
        #     if nums[l] == 0:
        #         while r <= len(nums)-1:
        #             if nums[r] != 0:
        #                 #Perform swap
        #                 nums[l] = nums[r]
        #                 nums[r] = 0
        #                 break
        #             r += 1
        #     l += 1
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                save = nums[fast]
                nums[fast] = nums[slow]
                nums[slow] = save
            if nums[slow] != 0:
                slow += 1
