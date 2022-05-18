class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check for size of the str
        #Check if each char is matching the str
        
        temp = list(t)
        if len(s) != len(t):
            return False
        for char in s:
            if char in temp:
                temp.remove(char)
        if len(temp) != 0:
            return False
        return True