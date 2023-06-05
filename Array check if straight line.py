class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if coordinates[1][0]-coordinates[0][0]==0:
            slope=None
        else:
            slope=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        for i in range(1,len(coordinates)-1):
            if coordinates[i+1][0]-coordinates[i][0]==0:
                temp_slope = None
            else:
                temp_slope = (coordinates[i+1][1]-coordinates[i][1])/(coordinates[i+1][0]-coordinates[i][0])           
                
            if temp_slope!=slope:
                return False
        return True