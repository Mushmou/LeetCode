class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if nums == []:
            return None

        freq = {}
        current = 0
        output = 0
        for elem in range( len(nums)):
            if nums[elem] in freq:
                freq[nums[elem]] = freq.get(nums[elem]) + 1
            else:
                freq[nums[elem]] = 1

            if freq.get(nums[elem]) + 1 > current:
                current = freq.get(nums[elem]) + 1
                output = nums[elem]
        return(output)