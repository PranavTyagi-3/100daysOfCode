class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        while True:
            if i%n==0 and i%2==0:
                return i
            i+=1