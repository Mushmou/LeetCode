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
        islandCount = 0

        def dfs(grid, r, c):
        #         Check if you are out of bounds or the current element is a zero
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return 0
            else:
                grid[r][c] = "0"
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)
            return 1
        
        #         Traverse the entire matrix
        #       We care about the 1 not a zero
        for r in range(rows):
            for c in range(columns):
                if (grid[r][c] == "1"):
                    islandCount += dfs(grid, r, c)
        return islandCount
    
