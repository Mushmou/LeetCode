#Check for rows, and columns for repetition (1-9)
#Check 3x3 sub boxes of the grid
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checkRowCol = collections.defaultDict(set)
        
        #Checking each row and column for duplicates (1-9)
        for r in range(len(board)):
            checkRow = set()
            checkCol = set()
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    if board[r][c] in checkRow:
                        return False
                    else:
                        checkRow.add(board[r][c])
                if board[c][r] != ".":
                    if board[c][r] in checkCol:
                        return False
                    else:
                        checkCol.add(board[c][r])
        #Check the grid
        for row in range(1,9,3):
            grid = set()
            for col in range(1,9,3):
                print(f"I am on {board[row][col]} pos {row} {col}")
                # print(grid)
                middle = board[row][col]
                # print(middle)
                top = board[row-1][col]
                # print(top)
                bot = board[row+1][col]
                # print(bot)
                right = board[row][col+1]
                # print(right)
                left = board[row][col-1]
                # print(left)
                topLeft = board[row-1][col-1]
                # print(topLeft)
                topRight = board[row-1][col+1]
                # print(topRight)
                botLeft = board[row+1][col-1]
                # print(botLeft)
                botRight = board[row+1][col+1]
                # print(botRight)
                
                if middle != ".":
                    if middle in grid:
                        return False
                    grid.add(middle)
                if top != ".":
                    if top in grid:
                        return False
                    grid.add(top)
                if bot != ".":
                    if bot in grid:
                        return False
                    grid.add(bot)
                if right != ".":
                    if right in grid:
                        return False
                    grid.add(right)
                if left != ".":
                    if left in grid:
                        return False
                    grid.add(left)
                if topLeft != ".":
                    if topLeft in grid:
                        return False
                    grid.add(topLeft)
                if topRight != ".":
                    if topRight in grid:
                        return False
                    grid.add(topRight)
                if botLeft != ".":
                    if botLeft in grid:
                        return False
                    grid.add(botLeft)
                if botRight != ".":
                    if botRight in grid:
                        return False
                    grid.add(botRight)
                grid.clear()
        return True
            
                
                