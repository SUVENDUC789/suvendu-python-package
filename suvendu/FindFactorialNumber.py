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
