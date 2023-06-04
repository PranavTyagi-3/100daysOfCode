class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=-1
        for i in range(1,len(nums)+1):
            c=0
            for j in nums:
                if j>=i:
                    c+=1

            if i==c:
                ans=i
                break
        return ans