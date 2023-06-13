class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=list(s)
        i=0
        j=len(li)-1
        while i<j:
            fr=li[i].lower()
            ba=li[j].lower()
            if fr in 'aeiou' and ba in 'aeiou':
                li[i],li[j]=li[j],li[i]
                i+=1
                j-=1
            elif fr in 'aeiou':
                j-=1
            elif ba in 'aeiuo':
                i+=1
            else:
                i+=1
                j-=1

        return "".join(li)