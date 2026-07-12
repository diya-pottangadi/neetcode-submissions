class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
"""
U:
- compare 2 strings
- return boolean
- the strings should have the same characters
P:
- edge case: if the lengths are difference, return false
- can i use a set to remove duplicates between the 2 strings
- or sort both strings so all the duplicates are next to each other, then compare
"""

