class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max=0
        i=0
        j=k-1
        count=0
        max=0
        for i in range(k):
            if s[i] in 'aeiou':
                count+=1
        max=count
        i=0
        while j!=len(s)-1:
            i+=1
            j+=1
            if s[i-1]=='a' or s[i-1]=='e' or s[i-1]=='i' or s[i-1]=='o' or s[i-1]=='u':
                count-=1
            if s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u':
                count+=1
            
            if count>max:
                max=count

        return max
