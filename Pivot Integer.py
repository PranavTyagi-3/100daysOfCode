class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        li=[i for i in range(1,n+1)]

        s=1
        e=n
        s1=s
        s2=e
        while s<e:

            if s1<s2:
                s+=1
                s1+=s
            elif s1>s2:
                e-=1
                s2+=e
            else:
                s+=1
                s1+=s
                e-=1
                s2+=e

        if s1==s2:
            return s
        else:
            return -1

