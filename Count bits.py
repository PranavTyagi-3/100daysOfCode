class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        li=[]
        for i in range(0,n+1):
            li.append(bin(i).count('1'))

        return li

        
