class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans=[0]*len(s)
        j=0
        for i in range(len(s)):
            ans[indices[i]]=s[j]
            j+=1
        return "".join(ans)