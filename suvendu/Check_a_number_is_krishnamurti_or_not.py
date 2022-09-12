# Check a number is krishnamurti or not.

def fact(n):
    p = 1
    for i in range(1, n+1):
        p = p*i
    return p

n = 145
n=int(input("Enter number : "))
temp = n
sum = 0
while n != 0:
    re = n % 10
    n = n//10
    sum=sum+fact(re)

if sum == temp :
    print(f"{temp} is krishnamurti number ")
else :
    print(f"{temp} is not krishnamurti number ")
