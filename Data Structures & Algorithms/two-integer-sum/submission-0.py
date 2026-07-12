class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        visited = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in visited:
                return [visited[complement], i]
            visited[num]=i

    '''
        left = 0
        right = len(nums)-1
        complete = False

        nums = sorted(nums)
        while not complete:
            t = nums[left] + nums[right]
            if t < target:
                left+=1
            if t > target: 
                right-=1
            
            if t==target:
                complete = True
                return [left, right]
            
    '''