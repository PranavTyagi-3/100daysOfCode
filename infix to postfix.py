<<<<<<< HEAD
stack=["("]
exp="A+(B*C-(D/E^F)*G)*H"
p=""
exp+=")"
def priority(x):
    if x=='^':
        return 1
    elif x=='*' or x=='/':
        return 2
    elif x=='+' or x=='-':
        return 3
for i in exp:
    if i=="(":
        stack.append(i)
    elif i.isalpha():
        p+=i
    elif i==")":
        while True:
            ele=stack.pop()
            if ele=="(":
                break
            p+=ele
    else:
        if len(stack)!=0:
            tmp=len(stack)-1
            while True:
                if stack[tmp]=="(":
                    break
                elif priority(stack[tmp])<priority(i):
                    p+=stack.pop()
                    tmp-=1
                elif tmp==[-1]:
                    break
                else:
                    break
        stack.append(i)

=======
stack=["("]
exp="A+(B*C-(D/E^F)*G)*H"
p=""
exp+=")"
def priority(x):
    if x=='^':
        return 1
    elif x=='*' or x=='/':
        return 2
    elif x=='+' or x=='-':
        return 3
for i in exp:
    if i=="(":
        stack.append(i)
    elif i.isalpha():
        p+=i
    elif i==")":
        while True:
            ele=stack.pop()
            if ele=="(":
                break
            p+=ele
    else:
        if len(stack)!=0:
            tmp=len(stack)-1
            while True:
                if stack[tmp]=="(":
                    break
                elif priority(stack[tmp])<priority(i):
                    p+=stack.pop()
                    tmp-=1
                elif tmp==[-1]:
                    break
                else:
                    break
        stack.append(i)

>>>>>>> 9b1a8378dd7fcc61a2069d5760e609db985dad2a
print(p)