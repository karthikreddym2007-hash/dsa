def countdown(n):
    print(n)
    if n==0:
        return 0
    else:
        return countdown(n-1)

n=int(input("enter number"))
print(countdown(n))
