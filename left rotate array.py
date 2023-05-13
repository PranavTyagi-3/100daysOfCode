def left_rotate(arr,d):     # Rotate array to left by d
    n=len(arr)
    for i in range(d):
        arr.append(arr.pop(0))


    return arr
print(left_rotate([1,2,3,4,5,6],2))