def insertion_sort(arr,n):
    for i in range(1,n):
        temp = arr[i]
        j=i-1
        while arr[j]>temp and j>=0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    print(arr)

insertion_sort([7,2,9,1],4)