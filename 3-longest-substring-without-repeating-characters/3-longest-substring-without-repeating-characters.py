'''
Understand
Match
Plan
make left, result, substring

iterate through the string, 
if the current element not in sub
    add elem to sub
otherwise
    get the index of the current element in the substring
    increment that index
    rewrite the subtring without that element and add the new element
    
    ie: current element = "b" substring ="bcd"
    output cbd
    
get the maxLength
return maxLength
Implement
Review
Evaluate

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        sub = ""
        
        for r in range(len(s)):
            if s[r] not in sub:
                sub += s[r]
            else:
                left = sub.index(s[r]) + 1
                print(f"left: {sub[left:]}, right {s[r]}")
                sub = sub[left:] + s[r]
            print(f'sub {sub} elem {s[r]}')
            res = max(res, len(sub))
        return res

            
            
            
            
            
            
            