class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result=[] # creating the resultant array
        self.backtrack(candidates,target,0,[]) # calling the backtrack function recursively with the candidates array
        return self.result # returning the resultant array

    def backtrack(self,candidates,currSum,i,path):
        if currSum == 0: # if current sum is equal to 0 then append the path array to the resultant array and return
            self.result.append(path[:])
            return
        
        if currSum<0 or i==len(candidates):# if current sum is less than 0 then return 
            return
        
        path.append(candidates[i]) # then append the candidates of ith value in path array

        self.backtrack(candidates,currSum-candidates[i],i,path[:]) # call the backtrack function recursively with current sum - candidates of ith value

        self.backtrack(candidates,currSum,i+1,path[:-1]) # calling the backtrack function recursively without choosing