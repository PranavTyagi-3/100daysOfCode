class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        while s.count("01")!=0:
            c+=1
            s=s.replace("01","10")

        return c