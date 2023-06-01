class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        li=[0,1]
        for i in range(1,n):
            li.append(li[-1]+li[-2])
        print(li)
        return li[n]
    
