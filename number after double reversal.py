<<<<<<< HEAD
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
=======
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
>>>>>>> 9b1a8378dd7fcc61a2069d5760e609db985dad2a
        return(str(rev)==str(num)[::-1])