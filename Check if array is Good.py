class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        m=nums[-1]
        for i in range(len(nums)-2):
            if nums[i]==nums[i+1]:
                return False

        if len(nums)!=m+1 or nums.count(m)!=2 :
            return False
        
        return True
        