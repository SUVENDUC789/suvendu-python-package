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
