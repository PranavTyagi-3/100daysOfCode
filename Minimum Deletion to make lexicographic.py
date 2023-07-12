class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        c=0
        for i in range(len(strs[0])):
            temp=[]
            for j in range(len(strs)):
                temp.append(strs[j][i])
            if temp!=sorted(temp):
                c+=1
        return c