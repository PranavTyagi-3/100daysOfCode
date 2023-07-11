class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=bin(n)[2:]
        temp=""
        for i in b:
            if i=='0':
                temp+='1' 
            else:
                temp+='0'
        
        return int(temp,2)