class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d_p={}
        pattern_n=""
        st_p=97
        for i in pattern:
            if i not in d_p:
                d_p[i]=chr(st_p)
                st_p+=1
            pattern_n+=d_p[i]
        

        new=""
        li=s.split(" ")
        d={}
        st=97
        for i in li:
            if i not in d:
                d[i]=chr(st)
                st+=1
            new+=d[i]

        if new==pattern_n:
            return True
        else:
            return False

        