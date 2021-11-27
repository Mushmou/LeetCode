class Solution(object):
    def reverse(self, x):
        sum = 0
        sign = 1
        
        if x < 0:
            sign = -1
            x = x*sign
        
        while x > 0:
            remainder = x % 10
            sum = (sum * 10) + remainder
            x = x//10
        
        check = sum * sign
        
        if check < -2147483648:
            return 0
        elif check > 2147483648:
            return 0
        
        return(check)