class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        li=[]
        for s in words:
            coded=""
            for i in s:
                pos = ord(i)-97
                coded+=codes[pos]

            if coded not in li:
                li.append(coded)
        
        return len(li)