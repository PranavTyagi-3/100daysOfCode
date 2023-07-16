class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_s=0
        a=0
        b=1
        c=1
        arr=[a,b,c]
        if n<3:
            return arr[n]
        for i in range(n-3):
            d=a+b+c
            arr.append(d)
            a,b,c=b,c,d
        
        return sum(arr[n-3:])