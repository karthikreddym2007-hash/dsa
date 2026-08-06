def search(A,k,n=0):
    if n>=len(A):
        return -1
    if A[n]==k:
        return n
    return search(A,k,n+1)
    



A=[1,2,3,4,5,6,7,8]
print(A)
k=int(input("enter id to search"))

print(search(A,k))
