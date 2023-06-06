class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        d=arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            temp_d = arr[i+1]-arr[i]
            if temp_d!=d:
                return False
        return True