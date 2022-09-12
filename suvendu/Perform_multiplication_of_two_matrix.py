# Perform multiplication of two matrix.
def Perform_multiplication_of_two_matrix():
    def ShowMatrix(a):
        for i in range(len(a)):
            for j in range(len(a[i])):
                print(a[i][j], end="  ")
            print("")


    def UserInput(a, r, c):
        for i in range(r):
            b = []
            for j in range(c):
                k = int(input(f"Enter number [{i}][{j}] : "))
                b.append(k)
            a.append(b)


    # [r1, c1] X [r2, c2] = [r1, c2] if c1 == r2

    def multiplication_of_two_matrix(a, b, r1, c1, r2, c2):
        c = []
        if c1 == r2:
            for i in range(r1):
                arr = []
                for j in range(c2):
                    arr.append(0)
                c.append(arr)

        if c1 == r2:
            print("multiplication of two matrix :>")
            for i in range(r1):
                for j in range(c2):
                    for k in range(c1):
                        c[i][j] = c[i][j] + (a[i][k]*b[k][j])

            ShowMatrix(c)
        else:
            print("multiplication not perform ")
            exit


    r1 = int(input("Enter row1 value : "))
    c1 = int(input("Enter coloumn1 value : "))
    a = []
    UserInput(a, r1, c1)
    print("First matrix are :>")
    ShowMatrix(a)

    r2 = int(input("Enter row2 value : "))
    c2 = int(input("Enter coloumn2 value : "))
    b = []
    UserInput(b, r2, c2)
    print("Second matrix are :>")
    ShowMatrix(b)

    multiplication_of_two_matrix(a, b, r1, c1, r2, c2)
