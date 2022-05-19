class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def findCoord(matrix):
            coords = []
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        x = (i,j)
                        coords.append(x)
                        # print(f'i: {i} j: {j}')
            return coords
        #Set the row
        def setRow(row, matrix):
            for i in range(len(matrix)):
                if i == row:
                    for j in range(len(matrix[i])):
                        # print(f'{i}{j}')
                        matrix[i][j] = 0
            
        def setCol(col, matrix):
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if j == col:
                        matrix[i][j] = 0
        
        def setMatrix(coords, matrix):
            x = setRow(coords[0], matrix)
            y = setCol(coords[1], matrix)
        
        coords = findCoord(matrix)
        
        for coord in coords:
            setMatrix(coord, matrix)
        
                    