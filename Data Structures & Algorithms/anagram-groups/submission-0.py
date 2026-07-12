class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        char = defaultdict(list)

        for string in strs:
            sort = ''.join(sorted(string))
            char[sort].append(string)
            
        return list(char.values())