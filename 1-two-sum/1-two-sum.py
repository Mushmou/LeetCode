class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = []
        
        for i in range(len(nums)):
            d.update( {i: nums[i]})
            
        vals= list(d.values())
        for i in range(len(nums)):
            print(f'Current num: {nums[i]}')
            print(f'{target} - {nums[i]} --> = {target-nums[i]}')
            if (target-nums[i]) in vals:
                if vals.index(target-nums[i]) != i:
                    res.append(i)
                    res.append(vals.index(target-nums[i]))
                    break
        print("")
        return res
                
            
            
            
            
            
            
            
            
            
            
            
                
        # for num in nums:
        #     prevKey = d.get(num)
        #     prevValue = num
        #     print(d)
        #     d.pop(num)
        #     print(d)
        #     if (target - num) in d:
        #         res.append(d.get (target-num) )
        #         print(f' {(target-num)} --> {d.get(target - num)}')
        #         res.append(dupeD.get(num))
        #         print(f' {(num)} --> {dupeD.get(num)}')
        #         break
        #     d.update( {prevValue: prevKey})
        # return(res)