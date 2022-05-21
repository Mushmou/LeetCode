'''
[
[1,2,3],
[4,5,6],
[7,8,9]
]

[
[1,2,3],
[4,5,6]
]
'''

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        output = []
        
        for i in range(m):
            output.append( n * [0] )
        print(output)
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                output[j][i] = matrix[i][j]
        return(output)