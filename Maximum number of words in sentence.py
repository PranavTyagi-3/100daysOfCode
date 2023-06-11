class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        m=0
        for i in range(len(sentences)):
            count=1
            for j in range(len(sentences[i])):
                if sentences[i][j]==' ':
                    count+=1
            if count>m:
                m=count
        return m