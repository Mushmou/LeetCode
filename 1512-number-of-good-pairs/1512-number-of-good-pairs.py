import collections
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #Equation  n * (n – 1) // 2
        res = 0
        freq = collections.defaultdict()
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        
        for num, occ in freq.items():
            if occ > 1:
                good_pairs = occ * (occ -1) // 2
                res += good_pairs
        return res