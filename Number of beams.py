class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        new=[]
        n=len(bank[0])
        for i in range(len(bank)):
            if bank[i]=="0"*n:
                continue
            new.append(bank[i])
        c=0
        for i in range(len(new)-1):
            c+=(new[i].count('1')*new[i+1].count('1'))

        return c
            

print("Hi")