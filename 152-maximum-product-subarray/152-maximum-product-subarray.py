class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct, minProduct, answer = 1, 1, nums[0]
        for num in nums:
            x = num*maxProduct
            maxProduct = max( (x), (num*minProduct), (num) )
            minProduct = min( (x), (num*minProduct), (num) )
            answer = max(maxProduct, answer)
        return answer