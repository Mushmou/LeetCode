class Solution:
    
    def toNum(c):
        num = ord(c)
        return num - 64
    
    def titleToNumber(self, columnTitle: str) -> int:
        #Get the least significant letter
        #answer += n * (26 * current iteration)
        def toNum(c):
            num = ord(c)
            return num - 64
        ans = 0
        base = 0
        for i in range(len(columnTitle)-1, -1, -1):
            ans += Solution.toNum(columnTitle[i]) * (26 ** base)
            base += 1
        return ans
