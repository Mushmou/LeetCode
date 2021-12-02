class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = []
        word_str = ""
        
#         for word in strs:
#             for char in word:
#                 word_str += char
        
#         for word in strs:
#             for char in word:                
#                 if word_str.count(char) == len(strs):
#                     if char not in prefix:
#                         prefix += char     
        
#         return prefix

        short = strs[0]
        for word in strs:
            if len(word) < len(short):
                short = word
        #shortest word
        
        maxprefix = []
        for word in strs:
            currentprefix = ""
            for i in range(len(short)):
                if short[i] == word[i]:
                    currentprefix += short[i]
                else:
                    break
            maxprefix.append(currentprefix)
            
        maxprefix.sort(key=len)
        return maxprefix[0]