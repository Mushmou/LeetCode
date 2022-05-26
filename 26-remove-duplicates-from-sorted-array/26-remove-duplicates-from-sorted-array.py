class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l = 1
        # for r in range(1, len(nums)):
        #     if nums[r] != nums[r-1]:
        #         nums[l] = nums[r]
        #         l+=1
        # return l
    
    
        left = 1
        right = 1
        
        while right != len(nums):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left +=1
            right +=1
        return left
    
    