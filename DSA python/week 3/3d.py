def merge_sort(a):
    if len(a)>1:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                a[k]=left[i]
                i+=1
            else:
                a[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            a[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            a[k]=right[j]
            j+=1
            k+=1

num=int(input("Enter number of elements: "))
a=[]
for i in range(num):
    x=int(input("Enter element: "))
    a.append(x)

print("Original array:",a)
merge_sort(a)
print("Sorted array:",a)
