class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        temp = list(moves)
        if temp.count('U')==temp.count('D') and temp.count('R')==temp.count('L'):
            return True
        else:
            return False