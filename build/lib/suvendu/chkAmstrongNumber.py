# Check a number is amstrong or not.

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
