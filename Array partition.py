class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        s=0
        while i<len(nums):
            s+=nums[i]
            i+=2
        return s
