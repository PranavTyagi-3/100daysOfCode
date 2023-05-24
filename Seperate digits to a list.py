class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=[]
        for i in nums:
            temp.extend(list(str(i)))
        ans = [int(i) for i in temp]
        return ans