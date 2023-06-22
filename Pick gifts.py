class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        while i<k:
            m=max(gifts)
            gifts[gifts.index(m)]=int(m**0.5)
            i+=1
        return sum(gifts)