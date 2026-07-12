class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        total = []
        p1 = 0
        while p1 < len(nums):
            s = 0
            p2 = p1
            while p2 < len(nums):
                s += nums[p2]
                total.append(s)
                p2 += 1
            p1 += 1
        return max(total)