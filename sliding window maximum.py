def maximum(arr,k):
    for i in range(0,len(arr)):
        if i+k>len(arr):
            break
        temp=arr[i:i+k]
        print(f"Maximum of {temp} is: {max(temp)}")


maximum([1, 2, 3, 1, 4, 5, 2, 3, 6],3)

