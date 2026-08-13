def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
                arr[i] , arr[min_index] = arr[min_index] , arr[i]
    return arr
num=int(input("Enter number of elements: "))
arr=[]
for i in range(num):
    x=int(input("Enter element: "))
    arr.append(x)
print("Sorted array is: ", selection_sort(arr))
