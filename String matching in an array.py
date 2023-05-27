class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans=[]
        for i in range(len(words)):
            li=words[:i]+words[i+1:]
            for j in li:
                if words[i] in j and words[i] not in ans:
                    ans.append(words[i])

        return ans