class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -pow(10,4)-1  # set to smallest integer value
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i];
            maxSum = max(maxSum, currSum);
            print('currSum: ' + str(currSum) + ', maxSum: ' + str(maxSum))
            if currSum < 0:
                currSum = 0

        return maxSum