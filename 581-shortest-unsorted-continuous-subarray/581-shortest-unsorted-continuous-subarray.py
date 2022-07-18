class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)
        sortedInput = sorted(nums)
        
        if nums == sortedInput or len(nums) == 1:
            return 0
        print(nums)
        print(sortedInput)

        # First find left
        for i in range(len(nums)):
            if nums[i] != sortedInput[i]:
                left = i
                break

        # First find right
        for j in range(len(nums)-1, -1, -1):
            if nums[j] != sortedInput[j]:
                right = j
                break

        # print(f'{right} : {left}')
        # print(f'{input[right]} : {input[left]}')
        return right+1 - left