class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = []
        
        for i in range(len(nums)):
            d.update( {i: nums[i]})
            
        vals= list(d.values())
        for i in range(len(nums)):
            # print(f'Current num: {nums[i]}')
            # print(f'{target} - {nums[i]} --> = {target-nums[i]}')
            if (target-nums[i]) in vals:
                if vals.index(target-nums[i]) != i:
                    res.append(i)
                    res.append(vals.index(target-nums[i]))
                    break
        return res