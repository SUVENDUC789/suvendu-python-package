# Remove the duplicate data from the list and print the list
n=int(input("Enter size of the list : "))
a=[]
for i in range(n):
    num=int(input(f"Enter number [{i}] : "))
    a.append(num)

print("Before Remove the duplicate element :>")
print("List element : ",a)
print("After Remove the duplicate element :>")
b=set(a)
b=list(b)
print("List element : ",b)
