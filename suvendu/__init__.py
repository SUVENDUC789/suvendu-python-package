def checkAmstrong(n):
    try:
        temp=n
        sum = 0
        order = len(str(n))
        while n != 0:
            re = n % 10
            n=n//10
            sum = sum+(re**order)

        if temp == sum:
            print(f" {temp} is amstrong number ")
        else :
            print(f" {temp} is not amstrong number ")
    except Exception as e:
        print("The error is : ",e)

def isLeapYear(year):
    if (year % 100 == 0 ) :
        print(f"{year} is not leap year ")
    elif (year % 400 == 0): 
        print(f"{year} is leap year ")
    elif(year % 4 == 0):
        print(f"{year} is leap year ")
    else:
        print(f"{year} is not leap year ")

def max_min_between_three_number(a,b,c):
    if a > b and a > c:
        print(f"Maximum value is : {a}")
    elif b > a and b > c:
        print(f"Maximum value is : {b}")
    elif c > a and c > b:
        print(f"Maximum value is : {c}")

    if a < b and a < c:
        print(f"Minimum value is : {a}")
    elif b < a and b < c:
        print(f"Minimum value is : {b}")
    elif c < a and c < b:
        print(f"Minimum value is : {c}")

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


# Check a number is palindrome or not.

def isNumberisPalindromeOrNot(n):
    p = 0
    temp=n
    while n != 0:
        re = n % 10
        n = int(n/10)
        p = (p*10)+re

    if p == temp:
        print(f"{temp} is palindrome number.")
    else:
        print(f"{temp} is not palindrome number.")


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)

def ItterativeApprochFactorialNumber(n):
    p = 1
    for i in range(1, n+1):
        p = p*i
    print(f"{n} ! = {p} (Itterative approch)")

def RecursiveApprochFactorialNumber(n):
    print(f"{n} ! = {fact(n)} (Recursive approch)")


# Check a matrix is magic square or not.
def matrix_is_magic_square_or_not(a, r, c):
    rowsum = []
    for i in range(r):
        rowsum.append(0)
        for j in range(c):
            rowsum[i] += a[i][j]

    # print("Row wise sum : ", rowsum)

    colsum = []
    for j in range(c):
        colsum.append(0)
        for i in range(r):
            colsum[j] += a[i][j]

    # print("Coloumn wise sum : ", colsum)

    digonal1 = 0
    digonal2 = 0

    for i in range(r):
        digonal1 += a[i][i]
        digonal2 += a[i][r-i-1]

    # print("Digonal-1 sum : ",digonal1)
    # print("Digonal-2 sum : ",digonal2)

    if rowsum == colsum:
        if digonal1 == digonal2:
            return 1
    else:
        return 0


def PrintMatrixElement(a):
    print(f"Matrix {len(a)} X {len(a[0])} :>")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print("")


def inputMatrix3X3_just_chek_magic_matrix_or_not():
    r = 3
    c = 3
    a = []
    print(f"Enter {r} X {c} Matrix element :>")
    for i in range(r):
        b = []
        for j in range(c):
            item = int(input(f"Enter number [{i}][{j}]: "))
            b.append(item)
        a.append(b)
    # PrintMatrixElement(a, r, c)

    if matrix_is_magic_square_or_not(a, r, c) == 1:
        print("matrix is magic square")
    else:
        print("matrix is not magic square")


