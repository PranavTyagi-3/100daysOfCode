class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for id, num in enumerate(nums):
            res.append(abs(sum(nums[:id]) - sum(nums[id + 1:])))

        return res