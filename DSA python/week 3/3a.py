def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
num=int(input("Enter number of elements: "))
arr=[]
for i in range(num):
    x=int(input("Enter element: "))
    arr.append(x)
print(arr)
print("Sorted array is: ",bubble_sort(arr))
