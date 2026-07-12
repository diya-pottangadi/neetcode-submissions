class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for s in strs:
            arr.append(str(len(s)))
            arr.append('#')
            arr.append(s)
        return "".join(arr)

    def decode(self, s: str) -> List[str]:
        arr = []
        i=0

        #format: 52#hello5#world
        while i<len(s):
            j=i
            #take in the number
            while s[j] != '#':
                j+=1
            length=int(s[i:j])
            #find the word, add it to the array
            i=j+1
            j=i+length
            arr.append(s[i:j])
            #reset and increment
            i=j
        return arr
            
