class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        st=0
        m=0
        for i in gain:
            st+=i
            if st>m:
                m=st

        return m