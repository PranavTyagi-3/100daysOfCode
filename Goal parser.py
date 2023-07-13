class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        s=""
        for i in range(len(command)):
            if command[i]=="G":
                s+="G"
            elif command[i]=="(":
                if command[i+1]==")":
                    s+="o"
                else:
                    s+="al"

        return s