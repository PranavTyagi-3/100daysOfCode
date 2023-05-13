def sorted_Stack(s):
        # Code here
        temp=[]
        for i in range(len(s)):
            temp.append(s.pop())
        temp.sort()
        for i in temp:
            s.append(i)
        print(s)



sorted_Stack([5,2,6,13,6,1])