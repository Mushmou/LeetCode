class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Where is the target if it is in the list
        #Where is the target if it is not in the list
        #Start from the middle
        l = 0
        r = len(nums)-1
        m = len(nums) // 2

        while l <= r:
            m = (r+l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
            
        if nums[m] > target:
            return m
        else:
            return m+1