# Find NcR where n,c,r are given as input.
# nCr = n! / (r! * (n-r)! ) 

def fact(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p


n=int(input("Enter number : "))
r=int(input("Enter number : "))
val= fact(n) / (fact(r) * fact(n-r))
print(f"{n}C{r} = {val}")
