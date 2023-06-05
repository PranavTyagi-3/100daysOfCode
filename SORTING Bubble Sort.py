def bubble_sort(li,n):
    for i in range(n-1):
        swapped = False
        for j in range(0,n-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                swapped = True
        if swapped == False:
            break
    print(li)

bubble_sort([1,4,7,9,11],5)