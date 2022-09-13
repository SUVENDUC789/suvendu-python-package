# Find NcR where n,c,r are given as input.
# nCr = n! / (r! * (n-r)! ) 

def C(n,r):
    def fact(n):
        p=1
        for i in range(1,n+1):
            p=p*i
        return p

    val= fact(n) / (fact(r) * fact(n-r))
    print(f"{n}C{r} = {val}")
