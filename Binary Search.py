def bin_s(li,n,ele):
    li.sort() 
    f=0
    k=0
    l=n-1  
    while f<=l:
        mi=(f+l)//2
        if li[mi]==ele:
            k=1
            break
        elif ele>li[mi]:
            f=mi+1
        elif ele<li[mi]:
            l=mi-1
    if k==1:
        print("FOUND")
    else:
        print("NOT FOUND")


l=[43,12,76,59,82,56,99]
n=len(l)
element=int(input("Enter ele to search: "))
bin_s(l,n,element)
