def Print3DMatrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(a[i][j])):
                print(a[i][j][k], end="  ")
            print("")
        print("")


'''
ThreeD = [
    [
        [1, 2, 3, 40],
        [4, 5, 6, 50],
        [7, 8, 9, 60]
    ],
    [
        [10, 20],
        [40, 50],
        [70, 80],
        [11, 12],
        [14, 15],
        [17, 18]
    ],
    [
        [100, 200, 300],
        [400, 500, 600],
        [700, 800, 900]
    ]
]

print("Example of 3-D Matrix :>")
ThreeDimentional(ThreeD)
'''


def input3DMatrix():
    a=[]
    r=int(input("Enter size of row : "))
    c1=int(input("Enter size of Row 1 : "))
    c2=int(input("Enter size of coloumn 2 : "))

    for i in range(r):
        c=[]
        for j in range(c1):
            b=[]
            for k in range(c2):
                val=int(input(f"Enter number [{i}][{j}][{k}] : "))
                b.append(val)
            c.append(b)
        a.append(c)
    
    return a
