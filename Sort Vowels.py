class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=[]
        for i in s:
            if i.lower() in 'aeiou':
                li.append(i)
        li.sort()
        i=0
        ans=""
        for char in s:
            if char in 'aeiouAEIOU':
                if char.islower():
                    ans+=li[i]
                else:
                    ans+=li[i]
                i+=1
            else:
                ans+=char
        return ans