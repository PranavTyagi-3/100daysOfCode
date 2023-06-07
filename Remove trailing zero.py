class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        j=-1
        if "0" not in num or num[-1]!="0":
            return num
        while num[j]=='0':
            j-=1
        return num[:j+1]