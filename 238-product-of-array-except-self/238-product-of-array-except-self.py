class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = []
        postfix = []
        
        product = 1
        productTwo = 1
        
        for i in range(len(nums)):
            product = product * nums[i]
            prefix.append(product)
        
        for i in range(len(nums)-1, -1, -1):
            productTwo = productTwo * nums[i]
            postfix.append(productTwo)
        
        postfix.reverse()
        firstIndex = 0
        lastIndex = len(nums)-1
        
        # print(prefix)
        # print(postfix)
        # print(len(nums))
        for i in range(len(nums)):
            outputProduct = 0
            # print('index num', nums[i], 'index', i)
            if i == firstIndex:
                outputProduct = (1 * postfix[i+1])
                output.append(outputProduct)
            # if nums[i] == nums[firstIndex]:
            #     outputProduct = (1 * postfix[i+1])
            #     output.append(outputProduct)
            elif i == lastIndex:
                outputProduct = (1 * prefix[i-1])
                output.append(outputProduct)
            # elif nums[i] == nums[lastIndex]:
            #     outputProduct = (1 * prefix[i-1])
            #     output.append(outputProduct)
            else:
                outputProduct = (prefix[i-1]) * (postfix[i+1])
                output.append(outputProduct)
            # print(output)
        return output