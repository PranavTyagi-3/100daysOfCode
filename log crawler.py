class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        st = ["Main"]
        for i in logs:
            if i[0].isalnum():
                st.append(i)
            elif i=='./':
                continue
            elif i=='../' and len(st)>1:
                st.pop()
        return len(st)-1
