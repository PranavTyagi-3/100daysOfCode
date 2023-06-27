class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        i=0
        j=n
        ans=[]
        while i<n:
            ans.append(nums[i])
            ans.append(nums[j])
            i+=1
            j+=1
        return ans