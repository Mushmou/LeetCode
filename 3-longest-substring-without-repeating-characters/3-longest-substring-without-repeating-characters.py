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
        l = 0
        res = 0
        sub = ""
        
        
        for r in range(len(s)):
            if s[r] not in sub:
                sub += s[r]
            else:
                print(f'sub {sub} right {s[r]}')
                left = sub.index(s[r]) + 1
                sub = sub[left:] + s[r]
            res = max(res, len(sub))
        return res

            
            
            
            
            
            
            