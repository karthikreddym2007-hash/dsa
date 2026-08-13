    def binary_search(a, low, high, key):
        while low <= high:
            mid = (low + high) // 2  
            
            if a[mid] == key:
                return mid  
            elif a[mid] > key:
                high = mid - 1  
            else:
                low = mid + 1  
        
        return -1  

    n = int(input("Enter number of elements: "))
    if n <= 0:
        print("Number of elements must be positive.")
    a = []
    for i in range(n):
        x = int(input("Enter element: "))
        a.append(x)
    a.sort()
    print("Sorted list:",a)
    key = int(input("Enter target element: "))
    result = binary_search(a, 0, len(a) - 1, key)
    if result != -1:
        print("Element found at index",result)
    else:
        print("Element not found.")
