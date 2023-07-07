class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ind=word.find(ch)
        if ind==-1:
            return word
        else:
            temp=word[:ind+1]
            temp=temp[::-1]
        return temp+word[ind+1:]