class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=s.split(" ")
        ans=[]
        for i in li:
            if len(i) != 0:
                ans.append(i)

        return ' '.join(ans[::-1])