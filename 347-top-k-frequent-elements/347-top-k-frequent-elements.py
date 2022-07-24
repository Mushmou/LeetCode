class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        num_map = {}

        if len(nums) == 1 and k == 1:
            return [ nums[0] ]

        for elem in nums:
            if elem not in num_map:
                num_map[elem] = 1
            else:
                num_map[elem] += 1

        swap = []
        for item in num_map.items():
            swap.append( (item[1], item[0] ))

        swap = sorted(swap)

        for i in range(k):
            result.append(swap[-1][1])
            swap.pop()
        return(result)