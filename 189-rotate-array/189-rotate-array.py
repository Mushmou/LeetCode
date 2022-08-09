'''
U
              1 2
nums = [1,2,3,4,5,6,7] k = 3

0 + 3
1 + 3

M
P
I
R
E
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        res = nums.copy()
        for i in range(len(nums)):
            print(res[i])
            nums[ (i + k) % len(nums) ] = res[i]
