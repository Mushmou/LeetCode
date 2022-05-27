class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #Check for even / odd numbers
        #Iterate through the list

        if len(nums) == 1:
            return nums
        left = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                temp = nums[i]
                nums[i] = nums[left]
                nums[left] = temp
                left +=1
        return nums