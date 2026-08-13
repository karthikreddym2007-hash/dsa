def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key
    return arr
num=int(input("Enter number of elements: "))
arr=[]
for i in range(num):
    x=int(input("Enter element: "))
    arr.append(x)
print(arr)
print("Sorted array is: ", insertion_sort(arr))
