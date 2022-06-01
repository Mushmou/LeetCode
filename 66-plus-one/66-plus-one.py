class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        place = 1
        for i in range(len(digits) - 1, -1, -1):
            num += digits[i] * place
            place *= 10
        
        num += 1
        return list(str(num))
