class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in ans:
                ans.append(nums1[i])

        return ans