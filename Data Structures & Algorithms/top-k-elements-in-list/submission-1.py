class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        most = []
        for key, value in freq.items():
            most.append([value, key])
        most.sort()

        res = []
        while len(res) < k:
            res.append(most.pop()[1])
        return res
            