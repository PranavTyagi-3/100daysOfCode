class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        if len(nums)==1:
            return []
        
        li=[]
        i=0
        while i <len(nums)-1:
            if nums[i]==nums[i+1]:
                li.append(nums[i])
                i+=1
            i+=1
        return li
                