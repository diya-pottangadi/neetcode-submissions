class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0

        left = 0 
        right = 1

        difference = []
        while left < (len(prices)-1):
            while right < len(prices):
                difference.append( prices[right] - prices[left] )
                right+=1
            left+=1
            right=left+1
        
        if max(difference)>0:
            return max(difference)
        return 0

'''
idea:
- left pointer
- right pointer

2 loops
right pointer continusouly starts over
appends the difference to an arrau
'''

