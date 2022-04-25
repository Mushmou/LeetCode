class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i,v = 0,1
        nums.sort()
        while v < len(nums):
            print(f' i = {nums[i]} index {i}')
            print(f' v = {nums[v]} index {v}')
            if nums[i] == nums[v]:
                return True
            i+=1
            v+=1
        return False
