class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sn = n*(n+1)/2
        s = sum(nums)

        return sn-s