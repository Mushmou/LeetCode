import collections
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        nums.sort()
        res = 0
        print(nums)
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    res += 1
        return res
        
#         #Equation  n * (n – 1) // 2
#         res = 0
#         freq = collections.defaultdict()
#         for i in range(len(nums)):
#             if nums[i] not in freq:
#                 freq[nums[i]] = 1
#             else:
#                 freq[nums[i]] += 1
        
#         for num, occ in freq.items():
#             if occ > 1:
#                 good_pairs = occ * (occ -1) // 2
#                 res += good_pairs
#         return res