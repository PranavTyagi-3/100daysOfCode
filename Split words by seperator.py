class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        ans=[]
        for i in words:
            ans.extend(i.split(separator))
        f_ans=[]
        for i in ans:
            if len(i)>=1:
                f_ans.append(i)
        return f_ans