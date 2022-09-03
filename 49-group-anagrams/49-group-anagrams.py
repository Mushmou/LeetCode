class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict()
        result = []
        for word in strs:
            if "".join(sorted(word)) not in anagrams:
                anagrams["".join(sorted(word))] = [word]
            else:
                anagrams.get("".join(sorted(word))).append(word)

        for anagramValue in anagrams.values():
            result.append(anagramValue)
        return result
    
#       Time Complexity O(n)
#       Space Complexity O(n)