def rangeBasedPrime(rangeofnumber):
    for i in range(rangeofnumber+1):
        flag = 0
        if i == 0 or i == 1:
            flag = 1
        for j in range(2, (int(i/2)+1)):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i,end="   ")

def isNumberisPrimeOrNot(n):
    flag = 0
    if n==0 or n==1 :
        flag=1

    for i in range(2,(int(n/2)+1)):
        if n % i ==0:
            flag=1
            break

    if flag==0:
        print(f"{n} is a prime number.")
    else :
        print(f"{n} is not a prime number.")
