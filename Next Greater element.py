class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums1:
            f=False
            for j in range(len(nums2)):
                if f and i<nums2[j]:
                    ans.append(nums2[j])
                    break

                if nums2[j]==i:
                    f=True

            else:
                ans.append(-1)

        return ans