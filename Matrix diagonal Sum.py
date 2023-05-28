class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        s=0
        i=0
        j=len(mat[i])-1
        k=0
        while j>-1:
            if i!=j:
                s+=mat[k][i]
                s+=mat[k][j]
            else:
                s+=mat[k][j]

            i+=1
            j-=1
            k+=1

        return s
