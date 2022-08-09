class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(row, target):
            left = 0
            right = len(row)-1
            
            while left <= right:
                mid = left + ((right-left) // 2)
                if row[mid] < target:
                    left = mid + 1
                elif row[mid] > target:
                    right = mid - 1
                else:
                    return True
            return False
                
        for row in matrix:
            if binarySearch(row,target) == False:
                continue
            else:
                return True