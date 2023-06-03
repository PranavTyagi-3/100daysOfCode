def ispossible(li, m, mid):
    student=1
    pages=0

    for i in range(len(li)):
        if pages+li[i] <= mid:
            pages+=li[i]
        else:
            student+=1
            if student>m or li[i]>mid:
                return False
            pages=li[i]

    return True

def book_alloc(li, m):
    sum_pages=sum(li)
    e=sum_pages
    s=0
    mid=s+(e-s)//2
    ans=-1
    while s<=e:
        

        if ispossible(li, m, mid):
            ans=mid
            e=mid-1
        else:
            s=mid+1
        
        mid=(s+e)//2

    return ans

print(book_alloc([10,20,30,40],2))