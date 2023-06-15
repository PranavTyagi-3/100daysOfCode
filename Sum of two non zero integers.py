class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):
            for j in range(i,n):
                if '0' not in str(i) and '0' not in str(j) and i+j==n:
                    return [i,j]