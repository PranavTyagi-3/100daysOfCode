queue = []
t=0

def q_push(x):
    queue.append(x)

def q_pop():
    if len(queue)==0:
        return -1
    return queue.pop(0)

# Implement stack using queue

def stack_push(x):
    q_push(x)

def stack_pop():
    n=len(queue)
    i=0
    while i<n-1:
        ele = q_pop()
        if ele == -1:
            break
        else:
            q_push(ele)
        i+=1
    q_pop()


stack_push(10)
stack_push(20)
stack_pop()
stack_push(30)
stack_push(40)
stack_pop()

print(queue)