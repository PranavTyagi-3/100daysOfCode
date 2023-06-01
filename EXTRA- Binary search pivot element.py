def pivot(li):
    s=0
    e=len(li)-1
    mid=s+(e-s)//2
    
    while s<e:
        if li[mid]>li[0]:
            s=mid+1
        else:
            e=mid

        mid = s+(e-s)//2

    return s

def binary_s(li,s,e,ele):
    
    while s<=e:
        mid=s+(e-s)//2
        if li[mid]>ele:
            e=mid-1
        elif li[mid]<ele:
            s=mid+1
        else:
            return mid
    return -1

def pivot_binary_search(li,key):
    
    if key>=li[pivot(li)] and key<=li[-1]:
        print(binary_s(li,s=pivot(li),e=len(li)-1,ele=key))
    else:
        print(binary_s(li,s=0,e=pivot(li)-1,ele=key))


pivot_binary_search([3,10,13,17,1,2],2)


#Approach
"""
Imagine the points on graph.
Pivot will be the minimum element.
The graph will be divided in two parts.
"""