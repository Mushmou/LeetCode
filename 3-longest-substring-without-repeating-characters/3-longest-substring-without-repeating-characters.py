class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Stuff to know
        #All inputs will be strings
        #Consist of letters, symbols, nums, spaces
        #Substring is string inside the main string.
        
        #Edge Cases
        #""z
        #"abcabcbb"
        #"bbbbb"
        #"pwwkew"
        #"123412"
        #"12$34%$12"
        #"12A34% $v2"
        
        # Make sure string is lowercase
        # Initialize two pointers, left and right
        # Create PREV and CURR
        # Iterate through main string, end when right pointer reaches the end
        # When iterating, if current elem is already in curr string and len(curr) > len(prev), set prev to curr.
        # Left = right
        # Right always moves up
        
        if len(s) == 1:
            return 1
        
        max_length, blue, temp = 0, 0, ""

        for pink in range(len(s)):
            if s[pink] not in temp:
                temp += s[pink]
            else:
                max_length = max(max_length, len(temp))
                blue = temp.index(s[pink]) + 1
                temp = temp[blue:] + s[pink]
        return max(max_length, len(temp))
