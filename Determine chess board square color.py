class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        letter, num = map(str, coordinates)
        if (ord(letter)%2 and int(num)%2) or (ord(letter)%2==0 and int(num)%2==0):
            return False
        return True