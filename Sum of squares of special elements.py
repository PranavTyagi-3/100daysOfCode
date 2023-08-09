class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sm=0
        n=len(nums)
        for i in range(1,len(nums)+1):
            if n%i==0:
                sm+=nums[i-1]*nums[i-1]
                
        return sm

            