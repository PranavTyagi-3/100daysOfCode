class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=0
        for i in num:
            n=n*10+i
        n+=k
        return [int(i) for i in str(n)]