'''
Understand

[2,7,11,15], target = 9
output [1,2]

[1,2,3,6] target = 5
output [2,3]

Edge Case
[-1,0], target = -1
output => [1,2]

Match

Plan
if right < target:
    if target - right == left:
        return [left, right]
    else:
        left += 1
right -= 1

Review
Evaluate
'''

'''
l   r
[-3,3,4,90]
0

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1,2]
        left = 0
        right = len(numbers)-1
        while left != right:
            print(f'left {numbers[left]} right {numbers[right]}')
            # # if numbers[right] <= target:
            print(f'target-right = {target - numbers[right]} : left {numbers[left]}')
            if target - numbers[right] > numbers[left]:
                left += 1
            elif target - numbers[right] == numbers[left]:
                return [left+1,right+1]
            # else:
            else:
                right -= 1