def find_duplicates(n,li):
    new=[]
    duplicates=[]
    for i in li:
        if i not in new:
            new.append(i)
        else:
            if i not in duplicates:
                duplicates.append(i)

    return duplicates

print(find_duplicates(9,[1,3,7,3,6,9,3,3,6]))
            