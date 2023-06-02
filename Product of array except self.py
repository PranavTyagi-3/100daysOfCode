class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prod=1
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            prod*=nums[i]

        ans=[]
        if nums.count(0)>1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                ans=[0]*len(nums)
                ans[i]=prod
                return ans
            else:
                ans.append(prod/nums[i])

        return ans