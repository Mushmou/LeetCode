class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = []
        postfix = []
        product, productTwo = 1, 1
        for i in range(len(nums)):
            product = product * nums[i]
            prefix.append(product)
        for i in range(len(nums)-1, -1, -1):
            productTwo = productTwo * nums[i]
            postfix.append(productTwo)
        postfix.reverse()
        firstIndex, lastIndex = 0, len(nums)-1
        for i in range(len(nums)):
            outputProduct = 0
            if i == firstIndex:
                outputProduct = (1 * postfix[i+1])
                output.append(outputProduct)
            elif i == lastIndex:
                outputProduct = (1 * prefix[i-1])
                output.append(outputProduct)
            else:
                outputProduct = (prefix[i-1]) * (postfix[i+1])
                output.append(outputProduct)
        return output