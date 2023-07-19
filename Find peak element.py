class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                return i
        return nums.index(max(nums))