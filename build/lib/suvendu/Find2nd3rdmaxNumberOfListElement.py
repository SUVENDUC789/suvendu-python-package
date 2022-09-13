# Find the 2nd ,3rd maximum of n number in the list.
# a=[9,6,7,4,28,2,0]

def Find2nd3rdmaxNumberOfList(a):
    a.sort()
    print("2nd maximum : ",a[len(a)-2])
    print("3rd maximum : ",a[len(a)-3])

