'''
Understand

# Can there be no island?
If yes return 0

# 
Match
Plan
Implement
Review
Evaluate
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        count_islands = 0
        
        def depth_first_search(grid, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
                return False
            grid[row][col] = "0"
            depth_first_search(grid, row+1, col) #Down
            depth_first_search(grid, row-1, col) #Up
            depth_first_search(grid, row, col+1) #Right
            depth_first_search(grid, row, col-1) #Left
            return True
        
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == "1":
                    dfs = depth_first_search(grid, row, col)
                    if dfs == True:
                        count_islands += 1
        return count_islands
