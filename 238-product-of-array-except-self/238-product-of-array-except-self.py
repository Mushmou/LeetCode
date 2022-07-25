class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        for i in range(len(nums)):
            if len(prefix) == 0:
                temp = nums[i]
            else:
                temp = prefix[-1] * nums[i]
            prefix.append(temp)

        for i in range(len(nums)-1, -1, -1):
            if len(postfix) == 0:
                temp = nums[i]
            else:
                temp = postfix[-1] * nums[i]
            postfix.append(temp)

        reversed_postfix = []

        for i in range(len(postfix)-1, -1, -1):
            reversed_postfix.append(postfix[i])
            
        result = []
        # Get output
        for i in range(len(nums)):
            if i == 0:
                result.append(reversed_postfix[i+1])
            elif i == len(nums)-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * reversed_postfix[i+1])
        return(result)