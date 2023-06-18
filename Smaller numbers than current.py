class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[j]<nums[i] :
                    c+=1
            ans.append(c)

        return ans
        
