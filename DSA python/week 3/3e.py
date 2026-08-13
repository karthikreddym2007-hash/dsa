def quicksort(a,low,high):
    if low<high:
        i=low
        j=high
        pivot=low

    while i<j:
        while i<len(a) and a[i]<=a[pivot]:
                               i+=1
        while a[j]>a[pivot]:
            j-=1
        if i<j:
            a[j],a[i]=a[i],a[j]
    a[j],a[pivot]=a[pivot],a[j]
    quicksort(a,low,j-1)
    quicksort(a,j+1,high)

num=int(input("Enter number of elements: "))
a=[]
for i in range(num):
    x=int(input("Enter element: "))
    a.append(x)
print(a)
n=len(a)
print("Sorted array is: ", quicksort(a,0,n-1))
    
