class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i=0
        j=0
        flag=0
        n=len(nums)
        ans=[]
        sm=sum(nums[:k*2])
        temp=k*2+1
        while i<n:
            if i<k or (n-i)<=k:
                ans.append(-1)
            else:
                if flag==0:
                    sm+=nums[i+k]
                    ans.append(sm//temp)
                    flag=1
                else:
                    sm+=nums[i+k]
                    sm-=nums[j]
                    ans.append(sm//temp)
                    j+=1
                    
            i+=1

        return ans
            
        