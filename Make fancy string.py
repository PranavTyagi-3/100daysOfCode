class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        i=0
        while i<len(s)-2:
            if s[i]==s[i+1]==s[i+2]:
                i+=1
            else:
                ans+=s[i]
                i+=1

        return ans+s[-2:]