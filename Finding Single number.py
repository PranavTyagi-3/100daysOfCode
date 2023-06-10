class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        while i<len(nums):
            if nums.count(nums[i])==3:
                i+=3
            else:
                break
        return nums[i]