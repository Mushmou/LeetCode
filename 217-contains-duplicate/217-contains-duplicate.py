class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if nums == None:
            return False
        
        dupes = []
        dupesSet = set(dupes)
        for num in nums:
            if num not in dupesSet:
                dupesSet.add(num)
            else:
                return True