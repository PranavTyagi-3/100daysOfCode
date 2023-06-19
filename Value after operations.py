class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        st=0
        for i in operations:
            if i=='--X' or i=='X--':
                st-=1
            else:
                st+=1

        return st
