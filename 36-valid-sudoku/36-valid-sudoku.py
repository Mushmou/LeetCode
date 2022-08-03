class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
        for row in range(1,9,3):
            grid = set()
            for col in range(1,9,3):
                directions = [
                    board[row][col],
                    board[row-1][col],
                    board[row+1][col],
                    board[row][col+1],
                    board[row][col-1],
                    board[row-1][col-1],
                    board[row-1][col+1],
                    board[row+1][col-1],
                    board[row+1][col+1],
                ]
                
                for direction in directions:
                    if direction != ".":
                        if direction in grid:
                            return False
                        else:
                            grid.add(direction)
                grid.clear()
                
                # middle = board[row][col]
                # top = board[row-1][col]
                # bot = board[row+1][col]
                # right = board[row][col+1]
                # left = board[row][col-1]
                # topLeft = board[row-1][col-1]
                # topRight = board[row-1][col+1]
                # botLeft = board[row+1][col-1]
                # botRight = board[row+1][col+1]
                
                # if middle != ".":
                #     if middle in grid:
                #         return False
                #     grid.add(middle)
                # if top != ".":
                #     if top in grid:
                #         return False
                #     grid.add(top)
                # if bot != ".":
                #     if bot in grid:
                #         return False
                #     grid.add(bot)
                # if right != ".":
                #     if right in grid:
                #         return False
                #     grid.add(right)
                # if left != ".":
                #     if left in grid:
                #         return False
                #     grid.add(left)
                # if topLeft != ".":
                #     if topLeft in grid:
                #         return False
                #     grid.add(topLeft)
                # if topRight != ".":
                #     if topRight in grid:
                #         return False
                #     grid.add(topRight)
                # if botLeft != ".":
                #     if botLeft in grid:
                #         return False
                #     grid.add(botLeft)
                # if botRight != ".":
                #     if botRight in grid:
                #         return False
                #     grid.add(botRight)
                # grid.clear()
        return True
            
                
                