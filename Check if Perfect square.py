class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=0
        j=num
        while i<=j:
            mid=(i+j)//2
            sq=mid*mid
            if sq==num:
                return True
            elif num<sq:
                j=mid-1
            else:
                i=mid+1
        return False