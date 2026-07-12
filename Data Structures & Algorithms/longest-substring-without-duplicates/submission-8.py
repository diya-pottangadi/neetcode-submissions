class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #plan
        #2 variables: one for length, one to hold substring
        #go through each character, if its in the substring, append the length of the substring to the counter variable and clear the substring, start again
        #edge case: if its empty, then 0
        
        lengths=[]
        substring=""
        if not s:
            return 0
        
        for c in s:
            if c in substring:
                lengths.append(len(substring))
                index=substring.find(c)
                substring=substring[index+1:]+c
            else:
                substring+=c

        lengths.append(len(substring))
        return max(lengths)

