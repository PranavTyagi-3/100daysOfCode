class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        

        while num>9:
            s=0
            while num>0:
                rem=num%10
                s+=rem
                num=num//10
            num=s

        return num