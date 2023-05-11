def subarray(arr1,sm):
    c=0
    for i in range(len(arr1)):
        for j in range(i,len(arr1)):
            if sum(arr1[i:j])==sm:
                c=1
                return arr1[i:j]
    if c==0:
        return -1

print(subarray([1, 4, 0, 0, 3, 10, 5],7))