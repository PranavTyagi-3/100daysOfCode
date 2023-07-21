class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j=len(s)-1
        li=list(s)
        while i<j:
            if li[i].isalpha() and li[j].isalpha():
                li[i],li[j]=li[j],li[i]
                i+=1
                j-=1
            if li[i].isalpha()==False:
                i+=1
            if li[j].isalpha()==False:
                j-=1

        return ''.join(li)
