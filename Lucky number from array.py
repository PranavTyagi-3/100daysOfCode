class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans=-1
        temp=[]
        for i in arr:
            if i not in temp:
                temp.append(i)
                if i==arr.count(i) and i>ans:
                    ans=i

        return ans