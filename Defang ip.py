class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans=""
        for i in range(len(address)):
            if address[i]=='.':
                ans+='[.]'
            else:
                ans+=address[i]

        return ans