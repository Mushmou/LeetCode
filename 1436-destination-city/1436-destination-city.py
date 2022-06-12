class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for elem in paths:
            d[elem[0]] = elem[1]

        # {B:C, D:B, C:A}
        flag = True

        for val in d.values():
            if val not in d.keys():
                return val
