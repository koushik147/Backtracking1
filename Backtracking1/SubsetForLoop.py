#TimeComplexity: O(n)
#SpaceComplexity: O(1)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]] # creating the resultant array

        for num in nums:
            size = len(result) # creating the size value
            for i in range(size):
                temp = result[i][:] # assigning the result of i value in the temp 
                #print(temp)
                temp.append(num) # append the num into the num
                result.append(temp) # append the temp value in the resultant array

        return result # returning the result
