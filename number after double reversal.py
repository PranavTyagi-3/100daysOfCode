class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        temp=num
        rev=0
        while temp>0:
            rev=rev*10+temp%10
            temp=temp//10
        return(str(rev)==str(num)[::-1])