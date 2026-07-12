class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        print(s)
        pointer1=0
        pointer2 = len(s)-1

        for i in range(len(s)):
            if s[pointer1]!=s[pointer2]:
                return False
            pointer2-=1
            pointer1+=1
            
        return True
"""
U - given a string of words
    - check if same forwards and backwards 
    - return boolean
P
- strip white spaces
- strip anything that isn't alphanumeric
- 2 pointers
    - pointer1 = 0
    - pointer 2 = len(str)-1
- compare the pointer
    - if not the same, return false

"""
