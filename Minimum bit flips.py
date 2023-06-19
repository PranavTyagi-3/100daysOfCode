class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        st = bin(start)[2:]
        g = bin(goal)[2:]
        l_st = len(st)
        l_g = len(g)
        if l_st>l_g:
            g='0'*(l_st-l_g)+g
        elif l_g>l_st:
            st='0'*(l_g-l_st)+st
        c=0
        for i in range(len(st)):
            if st[i]!= g[i]:
                c+=1

        return c

