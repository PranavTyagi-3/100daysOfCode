class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        s=0
        e=len(matrix)-1
        row=-1
        while s<=e:
            mid=(s+e)//2
            if target>matrix[mid][0] and target<matrix[mid][-1]:
                row=mid
                break
            elif target<matrix[mid][0]:
                e=mid-1
            elif target>matrix[mid][-1]:
                s=mid+1
            else:
                row=mid
                break
        
        for i in matrix[row]:
            if i==target:
                return True
        return False
        

        