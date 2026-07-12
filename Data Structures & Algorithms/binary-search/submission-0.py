class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if target < nums[mid]:
                right-=1
            if target > nums[mid]:
                left+=1
            if target==nums[mid]:
                return mid
        
        return -1
        
