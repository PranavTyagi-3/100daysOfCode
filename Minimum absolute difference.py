class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        ans=[]
        temp_min = arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff<temp_min:
                temp_min=diff
        
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==temp_min:
                ans.append([arr[i-1],arr[i]])
        
        return ans
