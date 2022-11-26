#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution(object):
    def subsets(self,nums):
        self.nums = nums # declaring the nums
        self.result = [] # creating the resultant array
        self.backtrack(0,[]) # calling the backtrack function recursively with 0 and empty array
        return self.result # returning the result
    
    def backtrack(self,pivot,path):
        self.result.append(path[:]) # appending the path array into result        
        
        for i in range(pivot,len(self.nums)):
            
            path.append(self.nums[i]) # appending the nums of ith element to path array
            self.backtrack(i+1,path) # calling backtrack function with incrementing i by 1

            path.pop() # popping the path array
