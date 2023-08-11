class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        nmin = num
        nmax = num
        num = str(num)
        for i in num:
            if i < '9':
                nmax = int(num.replace(i, '9'))
                break
        for i in num:
            if i != '0':
                nmin = int(num.replace(i, '0'))
                break
        return nmax - nmin