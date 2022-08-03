
import collections
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                elem = matrix[r][c]
                if elem in row[r] or elem in col[c]:
                    return False
                else:
                    row[r].add(elem)
                    col[c].add(elem)
        return True
    
        # for r in range(len(matrix)):
        #     row = set()
        #     col = set()
        #     for c in range(len(matrix[r])):
        #         if matrix[r][c] in row or matrix[c][r] in col:
        #             return False
        #         row.add(matrix[r][c])
        #         col.add(matrix[c][r])
        #     row.clear()
        #     col.clear()
        # return True