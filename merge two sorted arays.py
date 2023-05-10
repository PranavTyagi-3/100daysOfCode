def merge(arr1,m,arr2,n):
    i,j,k=0,0,0
    merged=[0]*(m+n)
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            merged[k]=arr1[i]
            k+=1
            i+=1
        else:
            merged[k]=arr2[j]
            k+=1
            j+=1

    if i<m:
        merged[k:]=arr1[i:]
    elif j<m:
        merged[k:]=arr2[j:]

    return merged


print(merge([1,3,6,9],4,[2,3,12],3))