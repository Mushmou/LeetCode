'''
Understand
Match
Plan
Implement
Review
Evaluate
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for n in nums:
            if n not in numbers:
                numbers.add(n)
            else:
                return True
        return False
