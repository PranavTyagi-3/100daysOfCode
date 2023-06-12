class Solution(object):
    def countConsistentStrings(self, allowed, words):
            """
            :type allowed: str
            :type words: List[str]
            :rtype: int
            """
            count=0
            for i in words:
                lab=True
                for j in i:
                    if j not in allowed:
                        lab=False
                        break
                if lab==True:
                    count+=1
            
            return count