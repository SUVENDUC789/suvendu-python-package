# Perform linear search for a given set of numbers in an list

def LinearSearch(a, value):
    j = -108
    for i in range(len(a)):
        if value == a[i]:
            return i
    return j


# a = [9, 6, 7, 4, 2, 8]
a=[]
n=int(input("Enter size of list : "))

for i in range(n):
    k=int(input(f"Enter Number [{i}] : "))
    a.append(k)

value = int(input("Enter searching element in your list : "))

if LinearSearch(a, value)==-108 :
    print(f"{value} not found !")
else :
    print(f"{value} is found at index {LinearSearch(a, value)}")

print("List element are : ",a)