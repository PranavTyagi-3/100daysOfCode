class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        li=[]
        li.extend([1]*numOnes)
        li.extend([0]*numZeros)
        li.extend([-1]*numNegOnes)
        
        return sum(li[:k])

        