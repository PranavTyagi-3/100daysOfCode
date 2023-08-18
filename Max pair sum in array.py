class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sm=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if max(str(nums[i]))==max(str(nums[j])):
                    print(nums[i],nums[j])
                    if nums[i]+nums[j]>sm:
                        sm=nums[i]+nums[j]
                        

        return sm