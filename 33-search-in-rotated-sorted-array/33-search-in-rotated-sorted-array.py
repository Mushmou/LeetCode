class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for count, value in enumerate(nums):
            if value == target:
                return count
        return -1