class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        for i in range(ord('a'),ord('z')+1):
            if chr(i) not in sentence:
                return False
        return True


        