class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        new=[]
        temp=[]
        for i in range(len(score)):
            temp.append(score[i][k])

        temp.sort(reverse=True)

        for j in temp:
            for l in score:
                if l[k]==j:
                    new.append(l)

        return new
