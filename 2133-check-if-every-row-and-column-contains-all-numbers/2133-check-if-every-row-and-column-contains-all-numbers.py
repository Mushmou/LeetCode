
import collections
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        
#         rows 
#         {
#             (1,2,3)
#             (3,1,2)
#             (2,3,1)
#         }
        
#         cols
#         {
#             (1,3,2)
#             (2,1,3)
#             (3,2,1)
#         }
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                elem = matrix[r][c]
                # print(f'elem {elem}')
                if elem in row[r] or elem in col[c]:
                    return False
                else:
                    row[r].add(elem)
                    col[c].add(elem)
                # print(f'row {row} col {col}')

        return True