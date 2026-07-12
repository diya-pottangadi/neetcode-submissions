class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #logic
        #for loop
        #check for a bigger number, add counter
        #edge case: last number, 0
        #edge case: if no bigger number, 0

        stack=[]
        counter=0

        for i in range(len(temperatures)-1):
            p=i+1
            counter=1
            found=False
            #find a way so that if nothing is greater, append 0
            while (p < len(temperatures)):
                if temperatures[p] > temperatures[i]:
                    stack.append(counter)
                    found=True
                    break
                
                p+=1
                counter+=1
            if not found:
                stack.append(0)

        stack.append(0)
        return stack
        
            

