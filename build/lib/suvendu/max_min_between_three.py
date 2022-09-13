def max_min_between_three_number(a,b,c):

    # a = int(input("Enter first number : "))
    # b = int(input("Enter second number : "))
    # c = int(input("Enter third number : "))

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
