class Solution(object):
    def closetTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n=len(words)
        cr=-1
        st_r=1
        cl=-1
        st_l=1
        i=(startIndex+1)%n
        j=(startIndex-1+n)%n
        if words[startIndex]==target:
            return 0
        while i!=startIndex:
            print(i)
            if words[i]==target:
                cr=i
                break
            st_r+=1
            i=(i+1)%n

        while j!=startIndex:
            if words[j]==target:
                cl=j
                break
            st_l+=1
            j=(j-1+n)%n

        if cr==-1:
            return -1
        else:
            return min(st_r,st_l)
        
