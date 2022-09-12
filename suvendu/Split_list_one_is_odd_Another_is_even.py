# Split the data of a list into two list where one list contain odd number and another list contain even number.
def split_two_list(a):
    even=[]
    odd=[]
    for i in range(len(a)):
        if a[i] % 2 ==0 :
            even.append(a[i])
        else:
            odd.append(a[i])
    return even,odd
    
if __name__=='__main__':
    n=int(input("Enter size of list : "))
    a=[]
    for i in range(n):
        item=int(input("Enter number :"))
        a.append(item)

    even,odd=split_two_list(a)
    print("Even values are : ",even)
    print("Odd values are : ",odd)
