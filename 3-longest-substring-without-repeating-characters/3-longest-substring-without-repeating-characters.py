'''
Understand
Match
Plan
Implement
Review
Evaluate
'''

'''
  l
     r
pwwkew
 l
    r
abcabcbb
l = 0
sub = ""
maxLength = 0
iterate through the string

if r not in sub:
    sub += right elem

if r in sub and last elem == s[r]:
    left = right
    right += 1
    sub = ""
    sub += left
    sub += right
else:
    get max(length of sub, maxLength)
    left += 1
    sub = [left:]
    right += 1
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
            
            
            
            
            
            
            
            
            