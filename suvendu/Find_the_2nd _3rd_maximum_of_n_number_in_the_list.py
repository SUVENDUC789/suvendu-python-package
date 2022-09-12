# Find the 2nd ,3rd maximum of n number in the list.
# a=[9,6,7,4,28,2,0]

a=[]
n=int(input("Enter size of your list : "))
for i in range(n):
    value=int(input(f"Enter number [{i+1}] : "))
    a.append(value)
print("List Element are : ",a)
a.sort()
# print(a)
print("2nd maximum : ",a[len(a)-2])
print("3rd maximum : ",a[len(a)-3])

