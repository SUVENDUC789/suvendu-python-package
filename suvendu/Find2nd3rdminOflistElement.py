# Find the 2nd ,3rd minimum of n number in the list.
# a=[9,6,7,4,28,2,0]

def Find2nd3rdminOflist(a):
    a.sort()
    print("2nd minimum : ",a[1])
    print("3rd minimum : ",a[2])