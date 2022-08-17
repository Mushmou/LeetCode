class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Where is the target if it is in the list
        #Where is the target if it is not in the list
        #Start from the middle
        
        #Check ends, 
        #Checking biggest
        if target > nums[-1]:
            return len(nums)
        
        if target <= nums[0]:
            return 0
        
        if target == nums[-1]:
            return len(nums)-1
        left = 0
        right = len(nums) -1 
        
        mid = left + ((right-left)//2)
        while (right - left != 1):
            mid  = left + ((right-left)//2)
            print(f"left: {left} mid: {mid} right: {right}")
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid
            
        return right
        print(f"left: {left} mid: {mid} right: {right}")