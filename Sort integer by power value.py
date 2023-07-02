class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        p=[]
        for i in range(lo,hi+1):
            c=0
            x=i
            while x!=1:
                if x%2==0:
                    x=x//2
                else:
                    x=3*x+1
                c+=1
            p.append([i,c])

        p.sort(key=lambda x:x[0])
        p.sort(key=lambda x:x[1])
        return p[k-1][0]
        