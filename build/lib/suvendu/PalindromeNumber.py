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
