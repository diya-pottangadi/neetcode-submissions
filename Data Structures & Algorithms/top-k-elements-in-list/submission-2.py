class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #for every element in the array, do a count, append to dictionary, sort in descending order, print the first k keys in an array
        
        order = {}

        unique = set(nums)
        for n in unique:
            count = nums.count(n)
            order[n]=count
        
        sorted_order = dict(sorted(order.items(), key=lambda item:item[1], reverse=True))

        output = []
        i=0
        keys = list(sorted_order.keys())

        while i <k:
            output.append(keys[i])
            i+=1
        return output


