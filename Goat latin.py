class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        ans=[]
        c=1
        for i in sentence.split():
            if i[0].lower() in 'aeiou':
                ans.append(i+'ma'+'a'*c)
            else:
                if len(i)>1:
                    ans.append(i[1:]+i[0]+'ma'+'a'*c)
                else:
                    ans.append(i+'ma'+'a'*c)

            c+=1

        return ' '.join(ans)