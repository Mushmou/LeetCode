class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        maxArea = 0
        for left in range(len(height)):
            for right in range(left+1, len(height)):
                # print(f'left: {left} right: {right}  height L: {height[left]} height R: {height[right]}')
                area = (right - left) * (min (height[left], height[right]) )
                maxArea = max(area, maxArea)
        # print(maxArea)
        return maxArea
        '''

        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            # print(f'left: {left} right: {right}  height L: {height[left]} height R: {height[right]} ')
            area = (right - left) * (min (height[left], height[right]) )
            maxArea = max(area, maxArea)
            # print(f'area: {area} maxArea: {maxArea}')
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
                
            