class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        #Add the last roman numeral to the answer
        ans = roman_map[s[-1]]
        
        #Reverse the loop
        for i in range(len(s)-2, -1, -1):
            print(f'{s[i]} : {s[i+1]} : {ans}')
            if roman_map[s[i]] >= roman_map[s[i+1]]:
                ans += roman_map[s[i]]
            else:
                ans = ans - roman_map[s[i]]
        return ans