class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        c1,c2=0,0
        i=0
        j=len(s)//2
        while j<len(s):
            if s[i].lower() in 'aeiou':
                c1+=1
            if s[j].lower() in 'aeiou':
                c2+=1
            i+=1
            j+=1
        
        return True if c1==c2 else False

        
