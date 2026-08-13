def linearSearch(a,key):
    for i in range(n):
        if a[i]==key:
            return i
    return -1

n=int(input("Enter number of elements"))
a=[]
for i in range(n):
    x=int(input("enter elements"))
    a.append(x)
key=int(input("Enter target element"))
print(linearSearch(a,key))
