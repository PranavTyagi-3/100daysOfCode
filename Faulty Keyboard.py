class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        for i in s:
            if i=="i":
                ans=ans[::-1]
            else:
                ans+=i

        return ans