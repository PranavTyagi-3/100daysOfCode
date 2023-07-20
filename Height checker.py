class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        exp=sorted(heights)
        c=0
        for i in range(len(heights)):
            if heights[i]!=exp[i]:
                c+=1
        return c