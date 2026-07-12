class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = list(set(nums))
        num.sort()

        cons = []
        i = 1
        counter=1

        if not nums:
            return 0

        while i < len(num):
            if num[i] == num[i-1]+1:
                counter+=1
            else:
                if counter>1:
                    cons.append(counter)
                counter=1
            i+=1
        cons.append(counter)
        return max(cons)
