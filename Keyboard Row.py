class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans=[]
        c=0
        for i in words:
            t=True
            if i[0].lower() in "qwertyuiop":
                c=1
            elif i[0].lower() in "asdfghjkl":
                c=2
            elif i[0].lower() in "zxcvbnm":
                c=3
            for j in i:
                j=j.lower()
                if c==1:
                    if j not in "qwertyuiop":
                        t=False
                        break
                elif c==2:
                    if j not in "asdfghjkl":
                        t=False
                        break
                elif c==3:
                    if j not in "zxcvbnm":
                        t=False
                        break
            if t:
                ans.append(i)
        
        return ans