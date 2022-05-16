class Solution:
    def isPalindrome(self, s: str) -> bool:

        
#        First remove all the excess characters that are not alphanumeric
        lowerStr = s.lower()
        str1 = ""
        for char in lowerStr:
            if char.isalnum():
                str1+=char

        print(str1)
#         Check forward as is backward (Monkey mode)
        str2 = ""
        for char in range(len(str1)-1, -1, -1):
            str2 += str1[char]
        
        if str1 == str2:
            return True
        else:
            return False
            
        