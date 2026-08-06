def power(p,n):
    if n<=0:
        return 1
    else:
        return p*power(p,n-1)
        
            
            

p=int(input("Enter prinipal"))
n=int(input("Enter number"))
print(power(p,n))
