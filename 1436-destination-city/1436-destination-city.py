class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for elem in paths:
            d[elem[0]] = elem[1]
        for val in d.values():
            if val not in d.keys():
                return val
