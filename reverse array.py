def reverse_array(arr):
    i=0
    j=len(arr)-1

    while i<j:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1

    return arr

print(reverse_array([1,2,3,4]))