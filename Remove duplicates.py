class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev=nums[0]
        c=0
        i=1
        while i<len(nums):
            if nums[i]==prev and c==0:
                c+=1
            elif nums[i]==prev and c==1:
                nums.pop(i)
                i-=1
            else:
                prev=nums[i]
                c=0
            i+=1
        return len(nums)