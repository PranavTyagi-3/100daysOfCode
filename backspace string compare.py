class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=[]
        t1=[]
        for i in s:
            if i=="#":
                if len(s1)==0:
                    continue
                else:
                    s1.pop()
            else:
                s1.append(i)
        
        for j in t:
            if j=="#":
                if len(t1)==0:
                    continue
                else:
                    t1.pop()
            else:
                t1.append(j)

        return True if s1==t1 else False
