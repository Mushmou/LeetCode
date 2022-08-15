# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n+1
        while left < right:
            mid = left + ( (right - left) // 2 )
            if isBadVersion(mid) == True:
                right = mid
            elif isBadVersion(mid) == False:
                left = mid + 1
            # print(mid, isBadVersion(mid), right, left)
        if left == right:
            return left
        else:
            return -1
                
                