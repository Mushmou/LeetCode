class Solution(object):
    def isPalindrome(self, var):
        
        var_original = var
        sum = 0
        while var > 0:
            remainder =  (var % 10)
            sum = (sum * 10) + remainder
            var = var // 10
            
        if var_original == sum:
            return True