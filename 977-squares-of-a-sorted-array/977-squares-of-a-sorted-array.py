class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        
        result = [0] * len(nums)
        index = len(nums)-1
        while l <= r :
            # print(result, nums[l]**2, nums[r]**2)
            if nums[l]**2 >= nums[r]**2:
                result[index] = nums[l]**2
                l += 1
            elif nums[r]**2 >= nums[l]**2:
                result[index] = nums[r]**2
                r -= 1
            index -= 1
        return result
            