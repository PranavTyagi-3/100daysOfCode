class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def pivot(li):
            s=0
            e=len(li)-1
            mid=(s+e)//2
            while (s<e):
                if li[mid]>li[e]:
                    s=mid+1
                else:
                    e=mid

                mid=(s+e)//2

            return s

        def binary_s(li,s,e,target):
            while s<=e:
                mid=(s+e)//2
                if li[mid]>target:
                    e=mid-1
                elif li[mid]<target:
                    s=mid+1
                else:
                    return mid
            return -1


        if target>=nums[pivot(nums)] and target<=nums[-1]:
            return(binary_s(nums,pivot(nums),len(nums)-1,target))
        else:
            return(binary_s(nums,0,pivot(nums)-1,target))