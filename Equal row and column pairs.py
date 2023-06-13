class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        col=[]
        for i in range(n):
            temp=[]
            for j in  range(n):
                temp.append(grid[j][i])
            col.append(temp)
        count=0

        for i in range(len(grid)):
            for j in range(len(col)):
                if grid[i]==col[j]:
                    count+=1
        return count