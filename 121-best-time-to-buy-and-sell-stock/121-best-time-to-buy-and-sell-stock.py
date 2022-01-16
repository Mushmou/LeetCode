class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        tempProfit = 0
        maxProfit = 0
        while left < len(prices) and right < len(prices):
            if prices[left] < prices[right]:    
                tempProfit = prices[right] - prices[left]
                maxProfit = max(tempProfit, maxProfit)
            else:
                left = right
            right += 1
        return maxProfit