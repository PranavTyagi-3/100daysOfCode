class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        i=0
        while i<len(min(strs)):
            j=1
            first=strs[0][i]
            while j<len(strs):
                if strs[j][i]!=first:
                    return ans
                j+=1
            ans+=strs[0][i]
            i+=1

        return ans
                