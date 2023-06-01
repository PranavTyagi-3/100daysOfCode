class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=0
        e=x
        ans=0
        while s<=e:
            mid=(s+e)//2
            if (mid*mid)<x:
                s=mid+1
                ans=mid
            elif (mid*mid)>x:
                e=mid-1
            else:
                return mid
        return ans
