def rangeOfPerfect():
    for n in range(1,10000):
        sum=0
        for i in range(1,n):
            if n % i ==0 :
                sum=sum+i

        if sum == n :
            print(f"{n} is perferct number.")

# rangeOfPerfect()
n=int(input("Enter number : "))
sum=0
for i in range(1,n):
    if n % i ==0 :
        sum=sum+i
if sum == n :
    print(f"{n} is perferct number.")
else :
    print(f"{n} is not perferct number.")
