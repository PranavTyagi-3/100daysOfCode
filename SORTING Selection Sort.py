def selection_sort(li):
    n=len(li)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if li[min_index]>li[j]:
                min_index=j


        li[i],li[min_index]=li[min_index],li[i]

    print(li)

selection_sort([6,2,8,4,10])
