# Split the data of a list into two list where one list contain odd number and another list contain even number.
def splitTwoListOneIsEvenAnotherIsOdd(a):
    even=[]
    odd=[]
    for i in range(len(a)):
        if a[i] % 2 ==0 :
            even.append(a[i])
        else:
            odd.append(a[i])
    return even,odd
